# gestor_stock.py

class GestorStock:

    def __init__(self, simbolo: str, nome: str, preco_atual=0.0, quantidade=0):
        self.__simbolo = simbolo
        self.__nome = nome
        self.__preco_atual = preco_atual
        self.__quantidade = quantidade

    @property
    def simbolo(self) -> str:
     #  """Devolve o símbolo da ação."""
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, valor: str):
     # """Define o símbolo da ação. O símbolo deve ser guardado e devolvido sem espaços adicionais e em maiúsculas."""
        self.__simbolo = valor.strip().upper()
        

    @property
    def nome(self) -> str:
     # """Devolve o nome da empresa."""
        return self.__nome
        

    @nome.setter
    def nome(self, valor: str):
     # """Define o nome da empresa."""
        self.__nome = valor.strip().title()


    @property
    def preco_atual(self) -> float:
     # """Devolve o preço atual da ação."""
        return self.__preco_atual
        

    @preco_atual.setter
    def preco_atual(self, valor: float):
     # """Define o preço atual da ação."""
        self.__preco_atual = float(valor) if valor > 0 else 0.0
        

    @property
    def quantidade(self) -> int:
     # """Devolve a quantidade de ações em carteira."""
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
     # """Define a quantidade de ações em carteira."""
        self.__quantidade = int(valor) if valor >= 0 else 0

    @property
    def preco_medio_compra(self) -> float:
     # """Devolve o preço médio de compra das ações em carteira."""
        return self.__preco_medio_compra

    @preco_medio_compra.setter
    def preco_medio_compra(self, valor: float):
     # """Define o preço médio de compra das ações em carteira."""
        self.__preco_medio_compra = float(valor)
        
    @property
    def lucro_realizado(self) -> float:
     #  """Devolve o lucro ou prejuízo relizado."""
        return self.__lucro_realizado

    @lucro_realizado.setter
    def lucro_realizado(self, valor: float):
     # """Define o lucro ou prejuízo relizado."""
        self.__lucro_realizado = float(valor)

    def comprar(self, quantidade: int, preco: float) -> bool:
     # """Realiza uma compra de ações.
        if quantidade <= 0 or preco <= 0:
            return False
        total_antigo = self.__preco_medio_compra * self.__quantidade
        total_novo = preco * quantidade
        nova_quantidade = self.__quantidade + quantidade

        self.__preco_medio_compra = (total_antigo + total_novo) / nova_quantidade
        self.__quantidade = nova_quantidade
        self.__preco_atual = preco

        return True

    def vender(self, quantidade: int, preco: float) -> bool:
     # """Realiza uma venda de ações.
        if quantidade <= 0 or preco <= 0:
            return False
        
        if quantidade > self.__quantidade:
            return False
        
        lucro = (preco - self.__preco_medio_compra) * quantidade
        self.__lucro_realizado += lucro

        self.__quantidade = self.__quantidade - quantidade
        self.__preco_atual = preco

        return True
    
    def valor_total(self) -> float:
     # """Calcula o valor total da posição na carteira (quantidade * preço_atual)."""
        return self.__quantidade * self.__preco_atual    

    def lucro_potencial(self) -> float:
     # """Apurar rentabilidade não realizada ao valor de cotação presente."""
        return (self.__preco_atual - self.__preco_medio_compra) * self.__quantidade
       
    def receber_dividendo(self, dividendo_por_acao: float) -> float:
     # """Apurar dividendos totais """
        if dividendo_por_acao <= 0:
            return 0.0
        
        montante = dividendo_por_acao * self.__quantidade
        self.__lucro_realizado += montante
        return montante
            