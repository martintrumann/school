import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False) 

br.set_debug_http(True)
br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Firefox')]
br.open('http://hotspot.ametikool.ee/login')
br.select_form( 'login' )
br.form[ 'username' ] = 'internet'
br.form[ 'password' ] = 'ametikool'
res = br.submit()

print(res)
