total = 0
 
print("--- 🍔 BEM-VINDO À LANCHONETE 🍟 ---")
print("Cardápio:")
print("Hambúrguer: R$ 10")
print("Refrigerante: R$ 5")
print("Batata Frita: R$ 7")
print("-----------------------------------")
 
while True:
    pedido = input("\nDigite o produto (ou 'finalizar' para encerrar): ").lower()
 
    if pedido == "finalizar":
        break  
    
 
    if pedido == "hamburguer":
        total += 10
        print("Item adicionado: Hambúrguer")
    elif pedido == "refrigerante":
        total += 5
        print("Item adicionado: Refrigerante")
    elif pedido == "batata frita":
        total += 7
        print("Item adicionado: Batata Frita")
    else:
 
        print("❌ Produto inválido! Tente novamente.")
 
 
print("-" * 35)
print(f"✅ Pedido encerrado!")
print(f"💰 Total da compra: R$ {total:.2f}")
print("-" * 35)