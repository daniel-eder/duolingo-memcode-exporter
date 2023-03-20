


# Broken API 

Duolingo-api is outdated. Login does not work, see https://github.com/KartikTalwar/Duolingo/issues/128#issuecomment-1449474903 for workaround:
https://github.com/KartikTalwar/Duolingo/blob/master/duolingo.py#L100, which then allowed me to instantiate like
lingo  = duolingo.Duolingo(username='myUsername', jwt='myJWT')

^ above fix is applied in https://github.com/daniel-eder/Duolingo/
Can be installed with "poetry add git+https://github.com/daniel-eder/Duolingo.git"



Get JWT Tken: document.cookie.match(new RegExp('(^| )jwt_token=([^;]+)'))[0].slice(11); 

