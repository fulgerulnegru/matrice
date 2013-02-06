class Matrix ():

    #initializam matricea
    def __init__ (self, matrix = None):
        if matrix :
            self.matrix = test(matrix)

        else:
            matrix = []
            t = []
            try:
                print "Se termina introducearea datelor printr-o line care contine doar enter"
                input_var = input("Linea matrici:")
                while True:
                    matrix.append(input_var)
                    input_var = input("Linea matrici:")
            except Exception as e:
                print "Am terminat de inregistrat matricea"

            self.matrix = test(matrix)

#testam daca este matrice
def test(mat):
    try:
        m = len(mat[0])
        if(m>0):
            for i in mat:
                if m != len(i):
                   return  'Difera numarul de coloane'
            return mat
        else:
            return "Nu este Matrice"
    except:
            return "Nu este Matrice"
