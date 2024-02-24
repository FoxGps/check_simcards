import pandas as pd

def check_iccid():
    # Ler os dados da planilha simcards.xlsx
    data_df = pd.read_excel('data/simcards.xlsx')

    # Ler os dados da planilha devices_com_ICCID.xlsx
    devices_df = pd.read_excel('data/devices_com_ICCID.xlsx')

    sem_match = []
    duplicado = []

    # Iterar sobre cada ICCID na planilha data.xlsx
    for iccid in data_df['ICCID']:
        # Contar quantas vezes o ICCID aparece na coluna phone da planilha devices_com_ICCID.xlsx
        count = devices_df['phone'].str.contains(iccid).sum()
        
        if count ==   0:
            # Se o ICCID não aparecer na coluna phone, adicionar à lista sem_match
            sem_match.append(iccid)
        elif count >   1:
            # Se o ICCID aparecer mais de uma vez na coluna phone, adicionar o DataFrame inteiro de devices_df que contém o ICCID duplicado à lista duplicado
            duplicado.append(devices_df[devices_df['phone'].str.contains(iccid)])

    sem_df = pd.DataFrame(sem_match, columns=['ICCID'])
    sem_df.to_excel('data/ICCID_sem_device.xlsx', index=False)

    # Concatenar todos os DataFrames duplicados em um único DataFrame
    dupli_df = pd.concat(duplicado, ignore_index=True)
    dupli_df.to_excel('data/ICCID_duplicado.xlsx', index=False)
    
    return sem_match, duplicado

if __name__ == "__main__":
    sem_match, duplicado = check_iccid()
    print("ICCIDs sem match:", len(sem_match))
    print("DataFrames de ICCIDs duplicados:", len(duplicado))