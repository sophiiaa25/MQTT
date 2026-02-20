README – Comunicação MQTT no Google Colab
Codigo feito no Colab 

Sobre o projeto
Este projeto demonstra como utilizar o protocolo MQTT para realizar comunicação entre aplicações usando Python no ambiente do Google Colab. O código cria um cliente MQTT que se conecta a um broker público, se inscreve em um tópico e permite tanto o envio quanto o recebimento de mensagens em tempo real. Esse tipo de comunicação é muito utilizado em projetos de Internet das Coisas, automação e sistemas distribuídos, pois o MQTT é um protocolo leve e eficiente para troca de mensagens entre dispositivos.

Tecnologias utilizadas
Neste projeto foram utilizadas a linguagem Python, a biblioteca Paho MQTT para realizar a comunicação via protocolo MQTT, o broker público HiveMQ como servidor intermediário para troca de mensagens e o ambiente Google Colab para execução do código diretamente no navegador, sem necessidade de instalação local de programas.

Instalação da biblioteca
No início do código é feita a instalação da biblioteca paho-mqtt utilizando o comando pip. Isso é necessário porque o Google Colab não vem com essa biblioteca instalada por padrão. Sem essa etapa, não seria possível criar o cliente MQTT e realizar a conexão com o broker.

Configuração do broker e do tópico
O código define o endereço do broker MQTT, que é o servidor responsável por receber e encaminhar as mensagens, a porta padrão utilizada pelo protocolo MQTT, que é a 1883, e o tópico que será usado para publicação e recebcrição das mensagens. O tópico funciona como um canal de comunicação, onde todos os clientes inscritos recebem as mensagens publicadas nesse mesmo endereço lógico.

Função de recebimento de mensagens
É criada uma função de callback chamada on_message. Essa função é executada automaticamente sempre que o cliente MQTT recebe uma nova mensagem no tópico em que está inscrito. Dentro dessa função, o conteúdo da mensagem recebida é exibido no terminal do Colab, permitindo que o usuário visualize em tempo real o que foi enviado por outros clientes ou por ele mesmo.

Criação e conexão do cliente MQTT
Após definir a função de callback, o código cria o cliente MQTT e associa essa função ao evento de recebimento de mensagens. Em seguida, o cliente se conecta ao broker usando o endereço e a porta definidos anteriormente. Depois da conexão, o cliente se inscreve no tópico escolhido, passando a receber todas as mensagens publicadas nesse canal.

Execução do loop de comunicação
O comando loop_start inicia o loop de comunicação em segundo plano. Esse loop é responsável por manter a conexão ativa com o broker e processar o envio e o recebimento de mensagens de forma contínua, sem travar a execução principal do programa.

Envio de mensagens
Por fim, o código entra em um laço infinito que solicita ao usuário que digite mensagens pelo teclado. Cada mensagem digitada é publicada no tópico configurado. Como o próprio cliente também está inscrito nesse tópico, ele recebe de volta as mensagens que enviou, além de receber mensagens enviadas por outros dispositivos ou aplicações conectadas ao mesmo broker e tópico.

Observações finais
Como o broker utilizado é público, qualquer pessoa que esteja inscrita no mesmo tópico poderá ver as mensagens enviadas. Em um ambiente real de produção, o ideal é utilizar um broker privado e aplicar autenticação e criptografia para garantir a segurança da comunicação.
