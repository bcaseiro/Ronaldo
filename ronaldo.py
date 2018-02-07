import cx_Oracle, getpass, sys, os
import xlwt, termcolor

def step1_USAGE():

    global username, hostlist, oraclerow, oraclecol

    if len(sys.argv) < 3 or len(sys.argv) > 3:
	    print ('------------------------------------------------------------------------')
	    print ('Invalid Arguments!')
	    print ('Usage   --> python ronaldo.py <<username>> <<path+filename>>')
	    print ('Example --> python ronaldo.py bcaseiro /tmp/serverlist.txt')
	    print ('Note: Oracle servers should be listed with its instance name, like the list below:\noracleserver01/xe\noracleserver02/dev\noracleserver03/production')
	    print ('------------------------------------------------------------------------')
            print (' ')
	    sys.exit()
  
    if len(sys.argv) == 3:
	if sys.argv[1] == '-h' or sys.argv[1] == '-H' or sys.argv[1] == '--h' or sys.argv[1] == '--H':
	    print ('------------------------------------------------------------------------')
	    print ('Invalid Arguments!')
	    print ('Usage   --> python ronaldo.py <<username>> <<path+filename>>')
	    print ('Example --> python ronaldo.py bcaseiro /tmp/serverlist.txt')
	    print ('Note: Oracle servers should be listed with its instance name, like the list below:\noracleserver01/xe\noracleserver02/dev\noracleserver03/production')
	    print ('------------------------------------------------------------------------')            
	    print (' ')
	    sys.exit()
	username = sys.argv[1]
	hostlist = sys.argv[2]
	PROCESSAR(username,hostlist)

def PROCESSAR(username,hostlist):

    oraclerow = 3
    oraclecol = 0

    wb = xlwt.Workbook()
    sheet2 = wb.add_sheet('SYSDBA and DBA Users', cell_overwrite_ok=True)
    style2 = xlwt.easyxf('pattern: pattern solid, fore_colour dark_blue;' 'font: colour white, bold True;')
    # Titulo
    sheet2.write_merge(0, 0, 0, 2, 'Privileged User Discovery for Oracle', style2)        

    # Cabecalho
    sheet2.write(2, 0, 'Version', style2)
    sheet2.write(2, 1, 'Oracle Server/Instance', style2)
    sheet2.write(2, 2, 'Username', style2)
    sheet2.write(2, 3, 'Privilege', style2)

    try:
    	targets = open(hostlist, 'r')
	targets.seek(0)
    	lines = targets.readlines()
	password = getpass.getpass('Password: ')
	
	print ('')
	print ('-------------------------------------------------------------------------------------')
	print ('Ronaldo - Privileged User Discovery tool for Oracle                                  ')
	print ('Finding Users with SYSDBA and DBA privileges. Please wait.   ')  
	print ('-------------------------------------------------------------------------------------')
	print ('') 
	for line in lines:
		try:

			conexao = cx_Oracle.connect(str(username)+'/'+str(password)+'@'+str(line))
			oracle_version = conexao.version
		
			cursor = conexao.cursor()
			cursor2 = conexao.cursor()
			cursor.execute("select username from dba_users where account_status = 'OPEN'")
			cursor2.execute("SELECT username FROM v$pwfile_users")
			
			for privuser in cursor2:
				trata_result2 = ''.join(privuser)
				trata1 = line.split('\n')
				trata3 = str(trata1[0])

				print ('SYSDBA User: ' + trata_result2 + ' - Oracle Instance: ' + trata3 + ' - Oracle Version: ' +str(oracle_version))
				sheet2.write(oraclerow, oraclecol, oracle_version)
                    		sheet2.write(oraclerow, oraclecol + 1, trata3)
                    		sheet2.write(oraclerow, oraclecol + 2, trata_result2)
				sheet2.write(oraclerow, oraclecol + 3, 'SYSDBA User')
				oraclerow = oraclerow +1
				wb.save('/tmp/PrivilegedAcccounts.xls')
	
			for result in cursor:
				trata_result = ''.join(result)	
				line2 = line.split('\n')
				line3 = str(line2[0])		
				print ('DBA User: ' + trata_result + ' - Oracle Instance: ' + line3 + ' - Oracle Version: ' +str(oracle_version))
				#print ('')
				oraclerow = oraclerow +1
				sheet2.write(oraclerow, oraclecol, oracle_version)
                    		sheet2.write(oraclerow, oraclecol + 1, line3)
                    		sheet2.write(oraclerow, oraclecol + 2, trata_result)
				sheet2.write(oraclerow, oraclecol + 3, 'DBA User')
				wb.save('/tmp/PrivilegedAcccounts.xls')
	
		except cx_Oracle.DatabaseError as err:
			line5 = line.split('\n')
			line6 = line5[0]			
			print 'Unable to connect to the Oracle Server: ', line6 + ' - Error: ', err
			print ('')


    except IOError as e:
    	#print(e.errno)
    	#print(e)
		print ('-------------------------------------------------------------')
    	print 'Error: Unable to read the file containing the list of hosts: ', hostlist
		print ('Please make sure the file exist and is accessible.')
    	print ('--------------------------------------------------------------')
	print ('')
    print ('')
    print ('-------------------------------------------------------------------------------------')
    print ('Scan was completed successfully. Please review the report /tmp/PrivilegedAccounts.xls')  
    print ('                             By Bruno Caseiro                                        ')
    print ('-------------------------------------------------------------------------------------')
    print ('')
   

step1_USAGE()
