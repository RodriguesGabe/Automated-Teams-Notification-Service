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
a cada hora.

Para configurá-lo:

1. No GitHub, abra o repositório e vá a **Settings → Secrets and variables →
   Actions**.
2. Clique em **New repository secret** e crie um segredo chamado
   `TEAMS_WEBHOOK_URL`. Cole a URL real do webhook como valor.
3. Faça push do workflow para a branch padrão do repositório.
4. Para testar sem esperar o cron, abra **Actions → Teams weather notification
   → Run workflow**.

O cron é interpretado em UTC. A expressão `0 * * * *` agenda o workflow no
início de cada hora UTC; o GitHub pode atrasar execuções agendadas em períodos
de alta demanda.
