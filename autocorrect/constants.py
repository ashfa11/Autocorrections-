word_regexes = {
    "en": r"[A-Za-z]+",
    #"ta": r"[அ-ஔக்-கௌங்-ஙௌச்-சௌஞ்-ஞௌட்-டௌண்-ணௌத்-தௌந்-நௌப்-பௌம்-மௌய்-யௌர்-ரௌல்-லௌவ்-வௌழ்-ழௌள்-ளௌற்-றௌன்-னௌ]",
    "ta": r"[அ-ஔக-ஹௗா-ூெ-ேை-்]+",
    
}

alphabets = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "ta": "அஆஇஈஉஊஎஏஐஒஓஔக்ககாகிகீகுகூகெகேகைகொகோகௌங்ஙஙாஙிஙீஙுஙூஙெஙேஙைஙொஙோஙௌச்சசாசிசீசுசூசெசேசைசொசோசௌஞ்ஞஞாஞிஞீஞுஞூஞெஞேஞைஞொஞோஞௌட்டடாடிடீடுடூடெடேடைடொடோடௌண்ணணாணிணீணுணூணெணேணைணொணோணௌத்ததாதிதீதுதூதெதேதைதொதோதௌந்நநாநிநீநுநூநெநேநைநொநோநௌப்பபாபிபீபுபூபெபேபைபொபோபௌம்மமாமிமீமுமூமெமேமைமொமோமௌய்யயாயியீயுயூயெயேயையொயோயௌர்ரராரிரீருரூரெரேரைரொரோரௌல்லலாலிலீலுலூலெலேலைலொலோலௌவ்வவாவிவீவுவூவெவேவைவொவோவௌழ்ழழாழிழீழுழூழெழேழைழொழோழௌள்ளளாளிளீளுளூளெளேளைளொளோளௌற்றறாறிறீறுறூறெறேறைறொறோறௌன்னனானினீனுனூனெனேனைனொனோனௌஃ",
}

ipfs_gateways = [
    "http://ipfs.io/ipfs/",
    "https://gateway.pinata.cloud/ipfs/",
    "https://cf-ipfs.com/ipfs/",  # this one has the best performance, but doesn't return download progress
]

ipfs_paths = {
    "en": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/en.tar.gz"],
}

backup_urls = {
    "en": [
        "https://dl.dropboxusercontent.com/s/grxjmtw4db814g1/en.tar.gz?dl=0",
    ],
    "ta": [
        "https://dumps.wikimedia.org/tawiki/20231120/tawiki-20231120-pages-articles-multistream.xml.bz2 ",
    ],
   
}