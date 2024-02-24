from utils import ler_planilha, api_connect, tem_19_digitos
import pandas as pd

def main():
    #FILTRAR PLANILHA DE SIM CARDS
    df = ler_planilha('data/simcards.xlsx')
    filtro = df['STATUS'] == 'ATIVO'
    dados_filtrados = df[filtro]
    
    path_simcards_filtrados = 'data/simcards_filtrados.xlsx'
    dados_filtrados.to_excel(path_simcards_filtrados, index=False)
    
    print(f"Dados filtrados salvos em {path_simcards_filtrados}")
    
    # Pega todo os devices registrados no token do usuario
    veiculos = api_connect()
    
    # Filtra todos os devices que tem ICCID Vinculado e salva na planilha devices_com_ICCID.xlsx
    device = [x for x in veiculos if tem_19_digitos(x['phone'])]
    df_devices = pd.DataFrame.from_dict(device)
    df_devices.to_excel('data/devices_com_ICCID.xlsx', index=False)
    if not df_devices.empty:
      print("Devices salvos em devices_com_ICCID.xlsx")
    
    ## Filtra os devices que tem menos de 7 digitos no campo Phone e salva na planilha devices_sem_phone.xlsx
    no_phone = [x for x in veiculos if len(x['phone']) <= 7]
    df_no_phone = pd.DataFrame.from_dict(no_phone)
    df_no_phone.to_excel('data/devices_sem_phone.xlsx', index=False)
    if not df_devices.empty:
      print("Devices salvos em devices_com_ICCID.xlsx")
    


if __name__ == "__main__":
    main()