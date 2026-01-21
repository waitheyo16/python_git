import pyodbc, logging, time
from p_configparser import Config


logger = logging.getLogger("Reader")
logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

ini_config = Config()
server, sanatorium_symbol = ini_config.ini_configparser_dozen()

server = server
database = 'mpharm'
username = 'sa'
password = 'pppp0619!@'

getcertinfo = [r'C:\Users\user\AppData\LocalLow\NPKI\user\cn=피에스알,ou=센터RA,ou=KICA고객센터,ou=등록기관,ou=licensedCA,o=KICA,c=KR\signCert.der', r'C:\Users\user\AppData\LocalLow\NPKI\user\cn=피에스알,ou=센터RA,ou=KICA고객센터,ou=등록기관,ou=licensedCA,o=KICA,c=KR\signPri.key']


def read_certificate_binary(file_path):
    try:
        # 'rb' 모드는 '읽기(r)' 및 '바이너리(b)'를 의미합니다.
        with open(file_path, 'rb' ) as f:
            # 파일 전체 내용을 bytes 객체로 읽어옵니다.
            binary_data = f.read()
        return binary_data
    except FileNotFoundError:
        logger.error(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {file_path}")
        return None
    except IOError as e:
        logger.error(f"파일 읽기 중 오류 발생: {e}")
        return None



def sql_update(binary):
    
    try:
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
        conn = pyodbc.connect(conn_str)        
        cursor = conn
        print("업데이트 스레드 쿼리 실행중 ")

        print(f'binary data {binary[0]}')
        print(f'binary data2 {binary[1]}')

        start_time = time.time()
        
        query = "INSERT INTO baseInfo_getcertInfo (cert_info_data, cert_info_key) VALUES  (?, ?)"
        # cursor.execute(query, binary[0], binary[1]) # INSERT query run twice 
        cursor.execute(query, (binary[0], binary[1])) # INSERT query run one        

        cursor.commit()

        
        end_time = time.time()  

        print(f" 업데이스레드트 (소요 시간: {end_time - start_time:.2f}초)")
        # print("스레드 results >>>", self._results)  

    except pyodbc.Error as ex:
      sqlsate = ex.args[0]
      # print(f"데이터베이스 연결 오류: {sqlsate}")
      return f"데이터베이스 연결 오류: {sqlsate}"
    finally:
        if conn:
           cursor.close()
          #  conn.close()
    # conn.close()      


if __name__ == '__main__':
  return_binary = []

  for path in getcertinfo:
      # print('path >>>' , path)
      logger.info('Path Data Read' , path)
      
      re_data = read_certificate_binary(path)
      return_binary.append(re_data)

      if return_binary:
          # print('return_binary append >>>> >>>>>')
          logger.info('Return Binary List Data')

      else:
          logger.error("파일 읽기 실패!!")



  # print('return binary apppend >>>>>', return_binary)
  logger.info('Return Binary Append Data >>', return_binary)
  # print('return binary type >>>', type(return_binary))

  # print('server = ', server)
  # print('DATABASE = ', database)
  # print('UID = ', username)
  # print('PWD = ', password)

  # conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
  # conn = pyodbc.connect(conn_str)

  sql_update(return_binary)


