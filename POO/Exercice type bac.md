# Exercice type bac

Cryptage selon le « Code de César »  

Dans cet exercice, on étudie une méthode de chiffrement de chaînes de caractères  alphabétiques. 

Pour des raisons historiques, cette méthode de chiffrement est appelée  "code de César". On considère que les messages ne contiennent que les lettres  capitales de l’alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ" et la méthode de  chiffrement utilise un nombre entier fixé appelé la clé de chiffrement.  

1. Soit la classe `CodeCesar` définie ci-dessous :  

   ```
   class CodeCesar:  
   	def __init__(self, cle):  
   		self.cle = cle  
   		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
   		
   	def decale(self, lettre):  
   		num1 = self.alphabet.find(lettre)  
   		num2 = num1+self.cle  
   		if num2 >= 26:  
   			num2 = num2-26  
   		if num2 < 0:  
   			num2 = num2+26  
   		nouvelle_lettre = self.alphabet[num2]  
   		return nouvelle_lettre   
   ```

   

   ​	On rappelle que la méthode `str.find(lettre)` renvoie l'indice (index) de la  `lettre` 		dans la chaîne de caractères `str`

    	Représenter le résultat d’exécution du code Python suivant : 

   ```
   code1 = CodeCesar(3)  
   print(code1.decale('A'))  
   print(code1.decale('X'))  
   ```

    

   2. La méthode de chiffrement du « code César » consiste à décaler les lettres du  message dans l’alphabet d'un nombre de rangs fixé par la clé. Par exemple,  avec la clé 3, toutes les lettres sont décalées de 3 rangs vers la droite : le A  devient le D, le B devient le E, etc.   

       Ajouter une méthode `cryptage(self, texte)` dans la classe` CodeCesar` définie  à la question précédente, qui reçoit en paramètre une chaîne de caractères (le  message à crypter) et qui retourne une chaîne de caractères (le message  crypté).  

      Cette méthode `cryptage(self, texte)` doit crypter la chaîne texte avec la clé  de l'objet de la classe `CodeCesar` qui a été instancié. 

      Exemple :

      ```
      >>>code1 = CodeCesar(3)  
      >>> code1.cryptage("NSI")  
      'QVL'  
      ```

      

   3. Ecrire un programme qui : 

      - demande de saisir la clé de chiffrement

      - crée un objet de classe ` CodeCesar` 

      -  demande de saisir le texte à chiffrer  

      -  affiche le texte chiffré en appelant la méthode `cryptage`

        

   4. On ajoute la méthode ` transforme(texte)` à la classe ` CodeCesar` :  

      ```
      def transforme(self, texte):  
      	self.cle = -self.cle  
      	message = self.cryptage(texte)  
      	self.cle = -self.cle  
      	return message
      ```

      On exécute la ligne suivante : `print(CodeCesar(10).transforme("PSX"))`

       Que va-t-il s’afficher ? Expliquer votre réponse.