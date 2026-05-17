# TROUBLESHOOTING REVERSO — 8 sintomas-âncora + matriz de confiança

A mentorada raramente chega dizendo "minha porta C falhou". Ela chega dizendo **"meu tráfego está caro"**, **"não consigo fechar venda"**, **"estou esgotada"**. A skill traduz sintoma em porta-fonte upstream.

Cada sintoma tem 1-3 portas candidatas. A confiança de cada candidata depende do contexto da mentorada (qual porta ela declarou concluída, qual métrica está fora da banda).

**Princípio diagnóstico:** Sintoma aparece downstream. Causa mora upstream. Skill devolve a porta-fonte mais provável + alternativas com confiança decrescente.

---

## SINTOMA 1 — Tráfego caro / CPA alto / ROAS < 3x

### ALTA confiança
- **Porta C (Causa)** — Mecanismo único fraco ou genérico. Sem mecanismo, headline não diferencia, criativo vira commodity, leilão pune.
- **Porta J (Jornada)** — Página de vendas com Bencivenga < 8. Não importa o tráfego — se a página não converte, CPA dispara.

### MÉDIA confiança
- **Porta D (Diferenciação)** — Sem 3 motivos pra escolher ela, anúncio compete só por atenção (preço sobe).
- **Porta H (Habitar)** — Tracking quebrado faz CPA parecer pior do que é (subestima conversão).

### BAIXA confiança
- **Porta K (Kombate)** — Otimização de ads ruim (mas geralmente é sintoma de C ou J, não causa).
- **Porta I (Imã)** — Falta de aquecimento orgânico (relevante em nicho frio).

### Ação seguinte
1. Audit C primeiro. Se C 13/13, vai pra J.
2. Se C e J ok, valida tracking H.
3. Só então mexe em K.

---

## SINTOMA 2 — Não fecha venda / lead não vira cliente

### ALTA confiança
- **Porta G (Garantia)** — Stack de valor fraco, garantia confusa, preço sem ancoragem.
- **Porta Q (Quartel)** — Time / processo de fechamento inexistente ou mal treinado.

### MÉDIA confiança
- **Porta B (Bússola)** — ICP errado: lead chega mas não é o público que compra.
- **Porta J (Jornada)** — Página atraiu lead frio que nunca ia comprar.

### BAIXA confiança
- **Porta D (Diferenciação)** — Lead compara e vai pro concorrente (raro virar causa principal).
- **Porta R (Recepção)** — Onboarding ruim em casos de upsell (não venda inicial).

### Ação seguinte
1. Se mentorada é solo: audit G + B.
2. Se tem time: audit Q (script, treinamento, KPIs).
3. Re-valida persona em B.

---

## SINTOMA 3 — Reembolso alto (> 5%)

### ALTA confiança
- **Porta R (Recepção)** — Onboarding D0-D7 falho. Aluno entra, não vê valor cedo, pede dinheiro de volta.
- **Porta F (Fundação)** — Programa não entrega o que vende. Promessa > realidade.

### MÉDIA confiança
- **Porta G (Garantia)** — Garantia generosa demais sem filtro de qualificação.
- **Porta B (Bússola)** — Vendendo pra Anti-Persona (público errado entra e pede reembolso).

### BAIXA confiança
- **Porta J (Jornada)** — Página vende uma promessa que o programa não cumpre (cascata J→F→R).
- **Porta Q (Quartel)** — Time vende a qualquer um pra bater meta.

### Ação seguinte
1. Audit R imediatamente (entrega rápida).
2. Audit F: programa cumpre o que J promete?
3. Reavalia B se persona errada está entrando.

---

## SINTOMA 4 — Burnout / esgotamento da mentorada

### ALTA confiança
- **Porta S (Servidores)** — Mentorada trabalha > 40h/semana cronicamente.
- **Porta O (Orquestra)** — Ainda responde primeiro, atende DM, e-mail, WhatsApp.

### MÉDIA confiança
- **Porta Q (Quartel)** — Time não fecha sozinho, mentorada vira closer reserva.
- **Porta M (Maestria)** — Funil exige intervenção diária.

### BAIXA confiança
- **Porta F (Fundação)** — Programa exige acompanhamento manual pesado da mentorada.

### Ação seguinte
1. Audit O, M e Q como bloco.
2. Identifica onde mentorada gasta a maior parte das horas.
3. Rollback pra porta-fonte (geralmente O ou Q).

---

## SINTOMA 5 — Margem baixa / lucro espremido

### ALTA confiança
- **Porta Y (Yield)** — Aquisição cara + estrutura inflada. Margem comprime.
- **Porta G (Garantia)** — Preço errado. Vendendo abaixo do valor entregue.

### MÉDIA confiança
- **Porta K (Kombate)** — CPA fora de banda (cascata J→K→Y).
- **Porta T (Tesouro)** — Sem reativação, todo cliente é cliente novo (LTV baixo).

### BAIXA confiança
- **Porta Q (Quartel)** — Time caro vendendo pouco.

### Ação seguinte
1. DRE 3-12 meses. Identifica linha que comprime.
2. Se aquisição: K e Y.
3. Se preço/oferta: G.
4. Se LTV: T.

---

## SINTOMA 6 — Conteúdo travado / fura calendário / sem inspiração

### ALTA confiança
- **Porta N (Narrativa)** — Calendário editorial não foi estruturado ou foi abandonado.

### MÉDIA confiança
- **Porta C (Causa)** — Sem mecanismo único, mentorada não sabe sobre o que falar (volta a postar genérico).
- **Porta E (Estandarte)** — Sem brand book / tom de voz, cada post é decisão nova (cansa).

### BAIXA confiança
- **Porta U (União)** — Comunidade não dá insumo orgânico (depende mais de N).

### Ação seguinte
1. Re-instala N como ciclo recorrente fixo.
2. Se N fixo e ainda trava: rollback C ou E.
3. Define template e cadência (não criatividade diária).

---

## SINTOMA 7 — Time desorientado / não cumpre / atritos

### ALTA confiança
- **Porta Q (Quartel)** — Time mal estruturado: sem KPI, sem script, sem rotina.
- **Porta Z (Zelo)** — Sem ciclo de melhoria + revisão, time perde direção.

### MÉDIA confiança
- **Porta F (Fundação)** — Programa não foi padronizado, time não sabe o que entregar.
- **Porta M (Maestria)** — Funil não documentado, time não sabe o que monitorar.

### BAIXA confiança
- **Porta E (Estandarte)** — Falta de identidade interna (relevante em times maiores).

### Ação seguinte
1. Audit Q (estrutura, KPI, rituais).
2. Liga ciclo Z mensal (`/reuniao-de-resultado`).
3. Se programa indefinido: F.

---

## SINTOMA 8 — Comunidade fraca / inativa / sem engajamento

### ALTA confiança
- **Porta U (União)** — Não foi cultivada, vira chat morto.

### MÉDIA confiança
- **Porta F (Fundação)** — Programa não cria momentos coletivos.
- **Porta P (Palco)** — Sem evento ao vivo, comunidade não tem energia recorrente.

### BAIXA confiança
- **Porta R (Recepção)** — Onboarding ruim faz aluno não chegar à comunidade ativo.

### Ação seguinte
1. Audit U: rituais, regras, moderação.
2. Se programa frio: F (criar marcos coletivos).
3. Se sem energia: P (evento próximo).

---

## MATRIZ DE CONFIANÇA — RESUMO

| Sintoma | Alta confiança | Média | Baixa |
|---|---|---|---|
| Tráfego caro | C, J | D, H | K, I |
| Não fecha venda | G, Q | B, J | D, R |
| Reembolso alto | R, F | G, B | J, Q |
| Burnout | S, O | Q, M | F |
| Margem baixa | Y, G | K, T | Q |
| Conteúdo travado | N | C, E | U |
| Time desorientado | Q, Z | F, M | E |
| Comunidade fraca | U | F, P | R |

---

## PROTOCOLO DE INVESTIGAÇÃO

Quando a mentorada declara um sintoma, a skill segue:

1. **Identifica sintoma-âncora** mais próximo dos 8.
2. **Lê dossiê** pra ver quais portas ela já declarou concluídas.
3. **Verifica porta de alta confiança** primeiro: se ela diz "C concluída", a skill duvida e pede evidência.
4. **Cruza com dependências** em `MAPA-DEPENDENCIAS.md`: se C é alta confiança e J está concluída, J pode estar contaminada também.
5. **Devolve diagnóstico** com confiança decrescente + ação.

---

## REGRA DURA

A skill **nunca recomenda mexer no sintoma diretamente sem auditar a porta-fonte**. Não otimiza criativo de K se C é a causa real. Não treina time de Q se F é a causa. Causa primeiro. Sintoma depois.

---

**Travessia Imperatriz — Pilar 2 (Fluxo). Propriedade intelectual Tata Gonçalves.**
