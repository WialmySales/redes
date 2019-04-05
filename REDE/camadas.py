#!/usr/bin/python3
# coding: utf-8
""" Classes das camadas TCP/IP """


class CdAplicacao():

    def __init__(self, camada):
        self.camada = camada
        # print("Camada TCP/IP: Aplicação")

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pela mensagem do processo"


class CdTransporte():

    def __init__(self, camada):
        if type(camada) == CamadaAplicacao:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pela comunicação processo-processo"


class CdInternet():

    def __init__(self, camada):
        if type(camada) == CamadaTransporte:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pelo roteamento"


class CdTransporte():

    def __init__(self, camada):
        if type(camada) == CamadaAplicacao:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pela comunicação processo-processo"

class CdFisica():

    def __init__(self, camada):
        if type(camada) == CamadaInternet:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável por troca com o meio físico"


 """Classe das camadas OSI"""

class CdFisicaOsi():

    def __init__(self, camada):
        self.camada = camada

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Transmissão e recepção dos bits brutos através do meio físico de transmissão"


class CdEnlaceOsi():

    def __init__(self, camada):
        if type(camada) == CdFisicaOsi:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Detecção de erros"


class CdRedeOsi():

    def __init__(self, camada):
        if type(camada) == CdEnlaceOsi:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Roteamento de pacotes em uma ou várias redes"


class CdTransporteOsi():

    def __init__(self, camada):
        if type(camada) == CdRedeOsi:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Oferece métodos para a entrega de dados ponto-a-ponto"

class CdSessaoOsi():

    def __init__(self, camada):
        if type(camada) == CdTransporteOsi:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Negociação e conexão com outros nós, analogia"

    class CdApresentacaoOsi():

        def __init__(self, camada):
            if type(camada) == CdSessaoOsi:
                self.camada = camada
            else:
                self.camada = None

        def desencapsular(self):
            return self.camada

        def responsabilidade(self):
            return "Formatação dos dados, conversão de códigos e caracteres"

    class CdAplicacaoOsi():

        def __init__(self, camada):
            if type(camada) == CdSessaoOsi:
                self.camada = camada
            else:
                self.camada = None

        def desencapsular(self):
            return self.camada

        def responsabilidade(self):
            return "Funções especialistas (transferência de arquivos, envio de e-mail, terminal virtual)"