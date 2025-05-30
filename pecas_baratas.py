import streamlit as st

# -------------------------------------------------------------- SIDEBAR
st.sidebar.title("Peças e seus preços")
pecas = ["AMD Ryzen 5 5600GT", "16GB DDR4", "SSD 480GB", "AMD Radeon RX 5500 XT", "Cooler para Processador T-Dagger Idun R, 90mm, LED Red, Intel-AMD, T-GC9109 R"]
peca = st.sidebar.selectbox("Selecione a peça",pecas)

# -------------------------------------------------------------- PRINCIPAL
st.title("Peças boas e baratas para PC")
if peca == "AMD Ryzen 5 5600GT":
    st.write('AMD Ryzen 5 5600GT')
elif peca == "16GB DDR4":
    st.write("16GB DDR4")
elif peca == "SSD 480GB":
    st.write("SSD 480GB")
elif peca == "AMD Radeon RX 5500 XT":
    st.write("AMD Radeon RX 5500 XT)")
elif peca == "Cooler para Processador T-Dagger Idun R, 90mm, LED Red, Intel-AMD, T-GC9109 R":
    st.write("Cooler para Processador T-Dagger Idun R, 90mm, LED Red, Intel-AMD, T-GC9109 R")
    st.markdown("""O Cooler para Processador T-Dagger Idun R (T-GC9109 R) é uma opção de entrada acessível para quem busca melhorar a refrigeração do processador com um toque 
                \nestético. Este cooler é compatível com diversos sockets de processadores Intel e AMD, tornando-o versátil para upgrades em sistemas mais antigos ou PCs de entrada.""")
    st.subheader("Especificações Técnicas :")
    st.write("""- Dissipador: 94 x 64 x 132 mm""")
    st.write("""- Fan (ventoinha): 90 x 90 x 25 mm""")