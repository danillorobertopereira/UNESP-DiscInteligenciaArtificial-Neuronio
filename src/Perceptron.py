import numpy as np

class Perceptron(object):
    """Classificador Perceptron.

    Parametros
    ------------
    eta : float
        Taxa de aprendizado (entre 0.0 e 1.0)
    n_iter : int
        Numero de passagens sobre o conjunto de treinamento.
    threshold : float
        Variavel limiar da funcao degrau 

    Atributos
    -----------
    w_ : array 1D
        Pesos apos o ajuste (incluindo a variavel de vies).
    errors_ : lista
        Numero de classificacoes incorretas em cada epoca.

    """
    def __init__(self, eta=0.01, threshold=0.5, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """Ajusta os dados de treinamento.

        Parametros
        ----------
        X : {array-like}, shape = [n_samples, n_features]
            Vetores de treinamento, onde n_samples eh o numero de amostras e
            n_features eh o numero de caracteristicas.
        y : array-like, shape = [n_samples]
            Valores alvo.

        Retorna
        -------
        self : objeto

        """
        

    def net_input(self, X):
        """Calcula a saída"""
        

    def predict(self, X):
        """Retorna o rotulo da classe apos a saida"""
        
