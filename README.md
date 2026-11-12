# Automated Teams Notification Service

Envia um Adaptive Card com as condições meteorológicas atuais de Recife para um grupo do Microsoft Teams.

## Executar localmente

1. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

2. Crie um arquivo `.env` na raiz do projeto e adicione a URL do webhook:

   ```env
   TEAMS_WEBHOOK_URL=sua_url_de_webhook
   ```

3. Execute:

   ```powershell
   python src/notifier.py
   ```

Não publique o arquivo `.env` nem compartilhe a URL do webhook.

## Agendamento pelo GitHub Actions

O workflow em `.github/workflows/teams-notification.yml` envia uma notificação
uma vez por mês, todo dia 9 às 09h no horário de Brasília. O workflow também
pode ser iniciado manualmente pela aba **Actions**.

Para configurá-lo:

1. No GitHub, abra o repositório e vá a **Settings → Secrets and variables →
   Actions**.
2. Clique em **New repository secret** e crie um segredo chamado
   `TEAMS_WEBHOOK_URL`. Cole a URL real do webhook como valor.
3. Faça push do workflow para a branch padrão do repositório.
4. Para testar sem esperar o cron, abra **Actions → Teams weather notification
   → Run workflow**.

O cron é interpretado em UTC. A expressão `0 12 9 * *` corresponde a 12h UTC
no dia 9 de cada mês, ou 9h no horário de Brasília (UTC−3). O GitHub pode
atrasar execuções agendadas em períodos de alta demanda.

Para mudar a frequência, edite o valor de `cron` no arquivo
`.github/workflows/teams-notification.yml`, faça commit e envie a alteração
para a branch padrão. Exemplos (todos em UTC):

| Expressão cron | Agendamento                         |
| -------------- | ----------------------------------- |
| `0 12 9 * *`   | Dia 9 de cada mês às 9h de Brasília |
| `0 12 * * *`   | Todos os dias às 9h de Brasília     |
| `0 * * * *`    | A cada hora, no minuto zero         |

Depois de alterar o cron, confira a conversão para UTC para que o envio ocorra
no horário local desejado. O botão **Run workflow** continua disponível para
execuções manuais, independentemente do cron.
