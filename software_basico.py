import os, zlib 

def compress(textfile,binfile):
    """
    :param textfile : arquivo texto 
    """
    try:    
        arquivo =  open(textfile,'rb')
        data = arquivo.read()
        compressed_data = zlib.compress(data)
        arquivo_bin = open(binfile,'wb')
        arquivo_bin.write(compressed_data)
    
    except Exception as e:
        print("erro\n")
    arquivo.close()
    arquivo_bin.close()

def decompress(binfile,textfile):
    try:
        with open(binfile,'rb') as arquivoBin:
            if isempty(file_path= binfile):
                return
            data_bin = arquivoBin.read()
            data_decompress = zlib.decompress(data_bin)
        with open(textfile,'wb') as arqtxt:
            arqtxt.write(data_decompress)
        
    
    except Exception as e:
        print('erro\n')
    arquivoBin.close()
    arqtxt.close()

def isempty(file_path):
    try: 
        file_size = os.path.getsize(file_path)
        if (file_size == 0):
            return True
        else:
            return False
    except FileNotFoundError as e:
        return




