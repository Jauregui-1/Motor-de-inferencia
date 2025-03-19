#RODRIGUEZ JAUREGUI JARED   

def modus_ponens(p, p_implica_q):
    """ 
    Aplica la regla de Modus Ponens: 
    Si P es verdadero y (P → Q) es verdadero, entonces Q es verdadero.
    """
    if p and p_implica_q:
        return True  # Q es verdadero
    return False  # No se puede concluir que Q sea verdadero

# Definir las premisas
P = True  # "Estudiaste"
P_IMPLICA_Q = True  # "Si estudias, aprobarás el examen"

# Aplicar Modus Ponens
Q = modus_ponens(P, P_IMPLICA_Q)

# Imprimir resultado
if Q:
    print("Conclusión: Aprobarás el examen.")  
else:
    print("No se puede concluir que aprobarás el examen.")
