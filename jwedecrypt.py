import sys
from jwcrypto import jwe
from jwcrypto import jwk
import base64

# rtfms:
#   https://tools.ietf.org/html/rfc7516#section-7.1
#   https://tools.ietf.org/html/rfc7517#page-5
#   https://jwcrypto.readthedocs.io/en/latest/index.html

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()

    # first argument is the jwe file to decrypt
    jwefile = open(sys.argv[1])
    jwefilecontents = jwefile.read()
    j = jwe.JWE()
    j.deserialize(jwefilecontents)

    # second argument is the key
    keystr = sys.argv[2]
    key = jwk.JWK()
    #key.from_pem(base64.b64decode(keystr)) #this fails
    #print(key)

    # do stuff
    #something = j.decrypt(key) # can't do this without a PWK object?
    #print(something)

