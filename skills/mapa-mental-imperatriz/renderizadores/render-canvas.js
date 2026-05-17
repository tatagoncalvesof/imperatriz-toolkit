#!/usr/bin/env node
// render-canvas.js — converte markdown hierárquico em Obsidian Canvas (.canvas)
//
// Uso: node render-canvas.js <input.md> <output.canvas>
//
// Estratégia:
//   1. Lê markdown
//   2. Extrai hierarquia de headings (#, ##, ###) + listas (-)
//   3. Gera nodes posicionados radialmente
//   4. Gera edges parent→child
//   5. Cores por ramo principal

const fs = require('fs');
const path = require('path');

const [, , inputFile, outputFile] = process.argv;

if (!inputFile || !outputFile) {
  console.error('Uso: node render-canvas.js <input.md> <output.canvas>');
  process.exit(1);
}

const content = fs.readFileSync(inputFile, 'utf-8');

// Remove frontmatter
const stripped = content.replace(/^---[\s\S]*?---\n/, '');

// Parse hierarquia
const lines = stripped.split('\n');
const tree = { id: 'root', text: '', children: [], level: 0 };
const stack = [tree];

for (const line of lines) {
  // Heading
  const headingMatch = line.match(/^(#{1,4})\s+(.+)$/);
  if (headingMatch) {
    const level = headingMatch[1].length;
    const text = headingMatch[2].trim();
    if (level === 1 && tree.text === '') {
      tree.text = text;
      continue;
    }
    const node = { id: `n${Math.random().toString(36).slice(2, 9)}`, text, children: [], level };
    while (stack.length > 1 && stack[stack.length - 1].level >= level) stack.pop();
    stack[stack.length - 1].children.push(node);
    stack.push(node);
    continue;
  }
  // Lista
  const listMatch = line.match(/^(\s*)[-*]\s+(.+)$/);
  if (listMatch) {
    const indent = listMatch[1].length;
    const text = listMatch[2].trim();
    const level = (stack[stack.length - 1].level || 1) + 1 + Math.floor(indent / 2);
    const node = { id: `n${Math.random().toString(36).slice(2, 9)}`, text, children: [], level };
    while (stack.length > 1 && stack[stack.length - 1].level >= level) stack.pop();
    stack[stack.length - 1].children.push(node);
    stack.push(node);
  }
}

// Gera layout radial
const nodes = [];
const edges = [];
const COLORS = ['1', '4', '5', '7', '2', '3', '6']; // rotação Imperatriz

// Root
nodes.push({
  id: tree.id,
  type: 'text',
  x: 0,
  y: 0,
  width: 280,
  height: 100,
  text: `# ${tree.text || 'Tema Central'}`,
  color: '6',
});

// Distribui ramos principais radialmente
const numRamos = tree.children.length;
const SPACING_V = 200;
const totalHeight = numRamos * SPACING_V;
let yOffset = -totalHeight / 2 + SPACING_V / 2;

tree.children.forEach((ramo, idx) => {
  const color = COLORS[idx % COLORS.length];
  const direction = idx % 2 === 0 ? 1 : -1;
  const ramoX = direction * 500;
  const ramoY = yOffset;
  yOffset += SPACING_V;

  nodes.push({
    id: ramo.id,
    type: 'text',
    x: ramoX - 110,
    y: ramoY - 40,
    width: 220,
    height: 80,
    text: `## ${ramo.text}`,
    color,
  });
  edges.push({
    id: `e-${tree.id}-${ramo.id}`,
    fromNode: tree.id,
    fromSide: direction > 0 ? 'right' : 'left',
    toNode: ramo.id,
    toSide: direction > 0 ? 'left' : 'right',
    color,
  });

  // Sub-ramos nível 2
  const numSubs = ramo.children.length;
  const subSpacingV = 110;
  let subY = ramoY - (numSubs * subSpacingV) / 2 + subSpacingV / 2;
  ramo.children.forEach((sub) => {
    const subX = ramoX + direction * 350;
    nodes.push({
      id: sub.id,
      type: 'text',
      x: subX - 100,
      y: subY - 30,
      width: 200,
      height: 60,
      text: sub.text,
      color,
    });
    edges.push({
      id: `e-${ramo.id}-${sub.id}`,
      fromNode: ramo.id,
      fromSide: direction > 0 ? 'right' : 'left',
      toNode: sub.id,
      toSide: direction > 0 ? 'left' : 'right',
      color,
    });

    // Nível 3 (folhas)
    const numLeaves = sub.children.length;
    const leafSpacing = 70;
    let leafY = subY - (numLeaves * leafSpacing) / 2 + leafSpacing / 2;
    sub.children.forEach((leaf) => {
      const leafX = subX + direction * 280;
      nodes.push({
        id: leaf.id,
        type: 'text',
        x: leafX - 90,
        y: leafY - 22,
        width: 180,
        height: 44,
        text: leaf.text,
        color,
      });
      edges.push({
        id: `e-${sub.id}-${leaf.id}`,
        fromNode: sub.id,
        fromSide: direction > 0 ? 'right' : 'left',
        toNode: leaf.id,
        toSide: direction > 0 ? 'left' : 'right',
        color,
      });
      leafY += leafSpacing;
    });

    subY += subSpacingV;
  });
});

const canvas = { nodes, edges };
fs.writeFileSync(outputFile, JSON.stringify(canvas, null, 2));
console.log(`  ✓ Canvas: ${outputFile} (${nodes.length} nós, ${edges.length} conexões)`);
