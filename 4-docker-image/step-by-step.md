# Desenvolvimento da imagem Docker para o AWS Lambda

O fluxo de desenvolvimento que iremos seguir tem os passos de:

1. Criar imagem Docker localmente;
2. Enviar imagem Docker local para o ECR;
3. Atualizar função Lambda com a imagem nova.

Para realizar esse fluxo, precisamos configurar do ambiente de desenvolvimento, ou seja:

1. Instalar Docker Engine;
2. Criar repositório no ECR;
3. Criar um IAM;
4. Instalar o AWS CLI.

---

## Configuração do ambiente de desenvolvimento

### Instalação do Docker Engine

No site oficial do Docker, você vai encontrar alguns métodos de instalação do Docker Engine para vários sistemas operacionais. Para sistemas Linux, por exemplo, um das maneiras de instalação é através do script https://get.docker.com:

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Criação do repositório no ECR

1. Na página [Amazon Elastic Container Registry](https://console.aws.amazon.com/ecr/repositories), clique em "Create repository";
2. Escolha a "Visibility settings" como "Private";
3. Em "Repository name", digite "forest-fire-classification" para nome o repositório;
4. Então, com tudo configurado, clique em "Create repository".

### Criação de IAM

1. Na página [IAM dashboard](https://console.aws.amazon.com/iam/), clique em "Users" e depois em "Add users";
2. Digite o nome de identificação do usuário em "User name";
3. Selecione o tipo de credencial "Access key - Programmatic access";
4. Anexe uma politica já existente em "AmazonEC2ContainerRegistryFullAccess" (apenas para este curso);
5. Clique em "Next" e depois em "Create user";
6. Baixe o arquivo CSV ou copie o "Access key ID" e o "Secret access key".

### Instalação do AWS CLI

Para enviar nossa imagem Docker local para o registro de imagens Docker da AWS, instale o AWS CLI:

```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

E, com o "Access key ID" e o "Secret access key" em mãos, configure sua credencial IAM com o AWS CLI:

```sh
aws configure
```

> AWS Access Key ID [None]: digite seu "Access key ID"
>
> AWS Secret Access Key [None]: disgite seu "Secret access key"
>
> Default region name [None]: digite sua região, exemplo: "us-west-2"
>
> Default output format [None]: json

---

## Desevolvimento da imagem Docker

### Criação a imagem Docker

1. Faça o login no Docker:

   ```sh
   aws ecr get-login-password --region <regiao> | docker login --username AWS --password-stdin <conta>.dkr.ecr.<regiao>.amazonaws.com
   ```

2. Copie o arquivo [4-docker-image/Dockerfile](Dockerfile);
3. Construa a imagem:

   ```sh
   docker build -t forest-fire-classification:1.0.0 .
   ```

### Envio para o ECR

1. Adicione uma tag nessa imagem:

   ```sh
   docker tag forest-fire-classification:1.0.0 <conta>.dkr.ecr.<regiao>.amazonaws.com/forest-fire-classification:1.0.0
   ```

2. E envie a imagem para o ECR:

   ```sh
   docker push <conta>.dkr.ecr.us-east-1.amazonaws.com/forest-fire-classification:1.0.0
   ```

### Atualização da imagem no Lambda

1. Vá para a página da sua função Lambda, clique na aba "Image", depois em "Deploy new image" e "Browse images";
2. Selecione o repositório "forest-fire-classification";
3. Escolha a versão nova (1.0.0) e clique em "Select image".


https://docs.docker.com/engine/install/ubuntu/#uninstall-docker-engine
https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html
https://docs.aws.amazon.com/pt_br/AmazonECR/latest/userguide/image-push.html
https://docs.aws.amazon.com/pt_br/lambda/latest/dg/images-create.html