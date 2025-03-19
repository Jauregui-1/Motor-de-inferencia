#RODRIGUEZ JAUREGUI JARED

def modus_tollens(p_implica_q, q):
    """ 
    Aplica la regla de Modus Tollens: 
    Si (P → Q) es verdadero y Q es falso, entonces P es falso.
    """
    if p_implica_q and not q:
        return False  # P es falso
    return None  # No se puede concluir nada sobre P

# Definir las premisas
P_IMPLICA_Q = True  # "Si llueve, el suelo estará mojado."
Q = False  # "El suelo NO está mojado."

# Aplicar Modus Tollens
P = modus_tollens(P_IMPLICA_Q, Q)

# Imprimir resultado
if P is False:
    print("Conclusión: No ha llovido.")  
else:
    print("No se puede concluir nada sobre la lluvia.")
