from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RX6KLE0TXH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-RX6KLE0TXH');
</script>
 """
 return prefix_google + "🪨 Welcome to the Dwayne Johnson Fan Club (DJFC) 🪨"
 