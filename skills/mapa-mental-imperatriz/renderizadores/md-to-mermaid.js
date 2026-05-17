#!/usr/bin/env node
// md-to-mermaid.js — converte markdown hierárquico (headings + listas) em bloco mermaid mindmap
//
// Uso: node md-to-mermaid.js <input.md>
// Output: imprime bloco mermaid no stdout

const fs = require('fs');
const [, , inputFile] = process.argv;

if (!inputFile) {
  console.error('Uso: node md-to-mermaid.js <input.md>');
  process.exit(1);
}

const content = fs.readFileSync(inputFile, 'utf-8');
const stripped = content.replace(/^---[\s\S]*?---\n/, '');

const lines = stripped.split('\n');
let root = 'Mapa Mental';
const tree = [];
const stack = [{ children: tree, level: 0 }];

for (const line of lines) {
  // # tema central
  const h1 = line.match(/^#\s+(.+)$/);
  if (h1) {
    root = h1[1].trim();
    continue;
  }
  // ## ramo principal
  const h2 = line.match(/^##\s+(.+)$/);
  if (h2) {
    const node = { text: h2[1].trim(), children: [], level: 2 };
    while (stack.length > 1 && stack[stack.length - 1].level >= 2) stack.pop();
    stack[stack.length - 1].children.push(node);
    stack.push(node);
    continue;
  }
  // ### sub-ramo
  const h3 = line.match(/^###\s+(.+)$/);
  if (h3) {
    const node = { text: h3[1].trim(), children: [], level: 3 };
    while (stack.length > 1 && stack[stack.length - 1].level >= 3) stack.pop();
    stack[stack.length - 1].children.push(node);
    stack.push(node);
    continue;
  }
  // - lista
  const list = line.match(/^(\s*)[-*]\s+(.+)$/);
  if (list) {
    const indent = list[1].length;
    const parentLevel = stack[stack.length - 1].level || 2;
    const level = parentLevel + 1 + Math.floor(indent / 2);
    const node = { text: list[2].trim(), children: [], level };
    while (stack.length > 1 && stack[stack.length - 1].level >= level) stack.pop();
    stack[stack.length - 1].children.push(node);
    stack.push(node);
  }
}

// Sanitiza pra evitar caracteres problemáticos no mermaid mindmap
function sanitize(text) {
  return text
    .replace(/\(([^)]*)\)/g, '$1')
    .replace(/[\[\]{}]/g, '')
    .replace(/["']/g, '')
    .replace(/:/g, '')
    .trim();
}

const out = [];
out.push('%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#9b59b6", "primaryTextColor": "#2c3e50", "lineColor": "#7f8c8d", "fontFamily": "Inter, sans-serif"}}}%%');
out.push('mindmap');
out.push(`  root((${sanitize(root)}))`);

function walk(nodes, depth) {
  for (const node of nodes) {
    const indent = '  '.repeat(depth + 2);
    out.push(`${indent}${sanitize(node.text)}`);
    walk(node.children, depth + 1);
  }
}
walk(tree, 0);

console.log(out.join('\n'));
