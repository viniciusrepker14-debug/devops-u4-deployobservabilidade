# API Flask - Deploy e Observabilidade

Projeto desenvolvido para a atividade U4 - Deploy e Manutenção de Back-end.

O projeto consiste em uma API desenvolvida em Python com Flask, com o objetivo de praticar testes automatizados, deploy na nuvem e monitoramento de uma aplicação.

## Tecnologias utilizadas

- Python
- Flask
- Pytest
- GitHub Actions
- Docker
- Docker Hub
- Render
- Better Stack

## Status do pipeline

![CI - API Flask](https://github.com/viniciusrepker14-debug/devops-u4-deployobservabilidade/actions/workflows/main.yml/badge.svg)

O GitHub Actions executa os testes automatizados e verifica a sintaxe do código. Quando uma alteração é enviada para a branch `main`, o pipeline também realiza a construção e publicação da imagem Docker e aciona o deploy no Render.

## API em produção

A aplicação está disponível em:

https://api-flask-devops.onrender.com

## Endpoints disponíveis

- `/` — retorna uma mensagem e o status da aplicação.
- `/produtos` — retorna uma lista de produtos.
- `/usuarios` — retorna uma lista de usuários.

## Testes automatizados

O projeto utiliza Pytest para executar os testes da API. Os testes são executados automaticamente pelo GitHub Actions durante o pipeline.

## Deploy

A aplicação é executada no Render, e sua imagem Docker é publicada no Docker Hub. O processo de deploy é integrado ao GitHub Actions, permitindo que as alterações enviadas para a branch `main` sejam publicadas após a execução da etapa de testes.

## Monitoramento

Foi utilizado o Better Stack para monitorar a disponibilidade dos três endpoints da API, com verificações periódicas e notificações por e-mail em caso de falhas detectadas.

Também foi realizado um teste de indisponibilidade do serviço para verificar o funcionamento dos alertas.

