import configparser

class Config():
  def __init__(self):
      pass

  def ini_configparser_write():
      file_path = r'C:\pharmdex\pharmdex.ini'
      config = configparser.ConfigParser() # 유니코드 문자열로 처리
      config['tpharm'] = {'value_1': 'True',
                      'value_2': '1',
                      'value_3': '1.0'}
      config['tpharm']['silson_server'] = '210.223.87.2'
      with open(file_path, 'w') as configfile:
          config.write(configfile)


  def ini_configparser():
      config = configparser.ConfigParser()
      file_path = r'C:\pharmdex\pharmdex.ini'     
      print('file_path >> ', file_path) 
      try:
        config.read(file_path, encoding='utf-8')
        # data = config.get['tpharm']['silson_server']
        data = config['tpharm']['silson_server']        
    
      except Exception as e:
        print(f"파일 읽기 오류: {e}")
      # exit()
      print('data >>', data )
      return str(data)
  

  def ini_configparser_dozen(self):
      config = configparser.ConfigParser()
      file_path = r'C:\pharmdex\pharmdex.ini'     
      print('file_path >> ', file_path) 
      try:
        config.read(file_path, encoding='utf-8')
        # data = config.get['tpharm']['silson_server']
        server = config['tpharm']['silson_server']
        medical_symbol = config['tpharm']['medical_symbol']
    
      except Exception as e:
        print(f"파일 읽기 오류: {e}")
      # exit()
      # print('data >>', data )
      return str(server), str(medical_symbol)
  

  def ini_configparser_GetPharmInfo():
        init={}
        config = configparser.ConfigParser()
        file_path = r'C:\pharmdex\pharmdex.ini'     
        print('file_path >> ', file_path) 
        try:
          config.read(file_path, encoding='utf-8')
          # data = config.get['tpharm']['silson_server']
          pharm_id = config['tpharm']['pharm_id']
          pharm_crn = config['tpharm']['pharm_crn']
          pharm_nm = config['tpharm']['pharm_nm']
          ceo_nm = config['tpharm']['ceo_nm']
          ceo_e_nm = config['tpharm']['ceo_e_nm']
          pharm_addr = config['tpharm']['pharm_addr']        
          pharm_tel = config['tpharm']['pharm_tel']                
      
        except Exception as e:
          print(f"파일 읽기 오류: {e}")
        # exit()
        # print('data >>', data )
        init['pharm_id'] = pharm_id
        init['pharm_crn'] = pharm_crn
        init['pharm_nm'] = pharm_nm
        init['ceo_nm'] = ceo_nm
        init['ceo_e_nm'] = ceo_e_nm
        init['pharm_addr'] = pharm_addr
        init['pharm_tel'] = pharm_tel

        return init

  def ini_configparser_Initialize2():
        init={}
        config = configparser.ConfigParser()
        file_path = r'C:\pharmdex\pharmdex.ini'     
        print('file_path >> ', file_path) 
        try:
          config.read(file_path, encoding='utf-8')
          # data = config.get['tpharm']['silson_server']
          pharm_id = config['tpharm']['pharm_id']
          pharm_crn = config['tpharm']['comp_crn']
              
      
        except Exception as e:
          print(f"파일 읽기 오류: {e}")
        # exit()
        # print('data >>', data )
        init['pharm_id'] = pharm_id
        init['comp_crn'] = pharm_crn

        return init


if __name__ == '__main__':
    
    db_host = Config()
    server, medical_symbol = db_host.ini_configparser_dozen()
    print('type >>' , (server, medical_symbol))
    



