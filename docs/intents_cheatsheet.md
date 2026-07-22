# Cheat Sheet - Intents do Agente CRM

> Intent é a ação de negócio final que o agente executa/comunica.

# Leads
---
* intent: `lead_criar` 
  * tool: `criar_lead`
  * exemplos: "Cadastre o Pedro da NexusAI...","Criar lead com email..."
  * data: {lead_id, name, email?, telefone?, empresa?}
  
* intent: `lead_obter`
  * tool: `obter_lead`
  * exemplos: "Selecione o lead do Pedro da NexusAI", "Abra o lead pedro@nexus.com"
  * data: {lead_id, nome, email?, telefone?, empresa?}

* intent: `lead_buscar`
  * tool: `buscar_lead`
  * exemplos: "Busque leads com NexusAI", "Busque o lead pedro@nexus.com"
  * data: {items: [{lead_id, nome, empresa}], total}

* intent: `lead_listar`
  * tool: `listar_lead`
  * exemplos: "Liste meus leads"
  * data: {items: [...], page?, limit?, total}

* intent: `lead_atualizar`
  * tool: `atualizar_lead`
  * exemplos: "Marque o Pedro como qualificado", "Atualiza o status para negociação"
  * data: {lead_id, campos_atualizados}

