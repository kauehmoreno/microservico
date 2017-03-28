# Aplicação microservico - Matéria
>Este é o projeto final de faculdade
>-Está aplicação servirá como base para o testes de performance entre aplicações monolíticas vs microserviço
>Aplicação Microserviço feita com tornado==4.4.2 e mongo com drive motor(assincrono)

`Cenários de testes entre arquiteturas`

| Testes | Ferramentas | arquitetura |
| -------| ----------- | ----------- |
| Números de requisições | apachebanchmark, pagespeedtest | Microserviço |
| Requisições paralelas | apachebanchmark | Microserviço |
| Tempo de resposta backend | usando modulo python, speedcurve | Microserviço |
| Tempo total de renderização | speedcurve PagesppedTest | Microserviço |
| Matérias com fotos | apachebanchmark,wrk, PagesppedTest | Microserviço |
| Materia com vídeos | apachebanchmark, wrk, PagesppedTest, speedcurve | Microserviço |

`Rotas da Aplicação`

| Função  |  parametros |
| -------- | ----------- |
| Todas as matérias | Filtro per_page, Filtro order_by(default será publicacao), uuid retorná uma única matéria |
| Rota para post | Rota que irá salvar as matérias criadas, aceitará uma lista quanto uma única matéria para procesar |

` Autor - Kauêh Moreno`

