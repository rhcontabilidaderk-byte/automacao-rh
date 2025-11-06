# automacao-rh

Scripts de RH e DP para cálculos automatizados.

## Ponto Raízes Humanas

O arquivo `ponto-raizes.html` entrega um espelho de ponto local com as seguintes características:

- Paleta visual nas cores verde + terracota, logo com fallback automático para o texto “Raízes Humanas”.
- PIN da diretoria `2468` para liberar Empresas, Colaboradores, Inserção manual, Limpar dia, Backup e Restauração.
- PIN do colaborador obrigatório para batidas (dispensado apenas em modo gestor ou após “Reconhecer agora”, que simula o facial por 5 minutos).
- Seed automático na primeira execução com a empresa Blessed, colaborador Bernardo e todas as marcações de outubro/2025.
- Exportação do período selecionado para espelho rápido, CSV simples, CSV folha (consolidado por dia + resumo semanal) e impressão/PDF.
- Backup e restauração do banco local (JSON) para preservar dados entre versões.

### Como usar rapidamente

1. Coloque `ponto-raizes.html` e (opcionalmente) `logo-raizes.jpg.png` na mesma pasta.
2. Abra o HTML em um navegador Chromium (Chrome/Edge).
3. Selecione empresa e colaborador; informe o PIN do colaborador para registrar marcações.
4. Use “Entrar modo gestor” com o PIN `2468` para cadastrar empresas/colaboradores, inserir marcações manuais, limpar dia ou gerar backup/restaurar.
5. Informe o período desejado (início/fim) para emitir espelho, exportar CSV (simples/folha) ou imprimir/salvar PDF.
