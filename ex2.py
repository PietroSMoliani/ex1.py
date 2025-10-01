def verificar_pedido(qtd_itens):
    if qtd_itens > 7:
        print("Pedido pronto")
        else:
            print("pedido insuficiente para envio")
            verificar_pedido(8)