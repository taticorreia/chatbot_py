import joblib
import utils
import sys

if __name__ == '__main__':
    
    print('Oi, eu sou o Chatbot. Em que posso ajudar?\n')
    while (True):
        # Ler texto e remover caracteres especiais.
        frase = input('... ')
        frase = utils.to_lower_remove_accents(frase)

        # Carregar o modelo de vetorizacao e aplicar no texto lido
        vectorizer = joblib.load('vectorizer.joblib')
        X = vectorizer.transform([frase])

        # Carregar o modelo de classificacao e aplicar no texto vetorizado
        classifier = joblib.load('classifier.joblib')
        predicted = classifier.predict(X)[0]

        # Maquina de estados do chatbot.
        if frase == 'sair':
            sys.exit(0)
        elif predicted == 'pagamento':
            print('\nPara obter mais detalhes sobre pagamentos e segundas vias, acesse:\nwww.minhaempresa.com.br/pagamentos')
        elif predicted == 'avaliacoes':
            print('\nPara obter mais detalhes sobre as avaliações, acesse:\nwww.minhaempresa.com.br/avaliações')
        elif predicted == 'tutoria':
            print('\nEstou encaminhando sua dúvida para a tutoria.')
        elif predicted == 'saudacao':
            pass