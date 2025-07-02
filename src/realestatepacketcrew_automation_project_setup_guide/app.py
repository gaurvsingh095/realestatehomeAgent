# import os
# from flask import Flask, request, jsonify, render_template_string
# from crew import RealestatepacketcrewAutomationProjectSetupGuideCrew

# app = Flask(__name__)

# # our one & only HTML template, served at /
# INDEX_HTML = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8" /><meta name="viewport" content="width=device-width,initial-scale=1"/>
#   <title>🏡 Packet Assistant</title>
#   <style>
#     :root {
#       --bg:#121212;--surface:#1f1f1f;--accent:#03dac6;
#       --text:#e0e0e0;--muted:#757575;--radius:8px;--trans:.3s;
#     }
#     *{box-sizing:border-box;margin:0;padding:0;}
#     body{background:var(--bg);color:var(--text);
#       font-family:sans-serif;display:flex;
#       justify-content:center;padding:2rem;}
#     .container{background:var(--surface);
#       border-radius:var(--radius);width:100%;
#       max-width:600px;padding:1rem;}
#     h1{text-align:center;color:var(--accent);margin-bottom:1rem;}
#     label{display:block;color:var(--muted);margin-top:.75rem;}
#     input, select, textarea {
#       width:100%;padding:.5rem;border:none;
#       border-radius:var(--radius);margin-top:.25rem;
#       background:#2a2a2a;color:var(--text);
#       transition:background var(--trans);}
#     input:focus, textarea:focus{outline:2px solid var(--accent);}
#     button{margin-top:1rem;padding:.75rem;
#       width:100%;background:var(--accent);
#       color:var(--bg);border:none;border-radius:var(--radius);
#       cursor:pointer;transition:background var(--trans);}
#     button:disabled{background:var(--muted);cursor:default;}
#     .spinner{display:none;margin:1rem auto;
#       width:32px;height:32px;border:4px solid var(--muted);
#       border-top-color:var(--accent);border-radius:50%;
#       animation:spin 1s linear infinite;}
#     @keyframes spin{to{transform:rotate(360deg);}}
#     .result{white-space:pre-wrap;
#       background:#222;padding:.75rem;
#       border-radius:var(--radius);margin-top:1rem;
#       max-height:300px;overflow:auto;}
#   </style>
# </head>
# <body>
#   <div class="container">
#     <h1>Packet Assistant</h1>
#     <label>Name<input type="text" id="client_name" /></label>
#     <label>Budget<input type="text" id="budget" /></label>
#     <label>Neighborhood<input type="text" id="neighborhood" /></label>
#     <label>Bedrooms<input type="number" id="bedrooms" min="1"/></label>
#     <label>Timing<input type="text" id="timing" /></label>

#     <button id="runBtn">Generate Packet</button>
#     <div class="spinner" id="spinner"></div>
#     <div class="result" id="output"></div>
#   </div>

#   <script>
#     const runBtn = document.getElementById('runBtn'),
#           spinner = document.getElementById('spinner'),
#           output  = document.getElementById('output');

#     runBtn.onclick = async () => {
#       // gather inputs
#       const payload = {
#         client_name:  document.getElementById('client_name').value,
#         budget:       document.getElementById('budget').value,
#         neighborhood: document.getElementById('neighborhood').value,
#         bedrooms:     parseInt(document.getElementById('bedrooms').value)||0,
#         timing:       document.getElementById('timing').value
#       };

#       runBtn.disabled = true;
#       spinner.style.display = 'block';
#       output.textContent = '';

#       try {
#         const res = await fetch('/api/run', {
#           method:'POST',
#           headers:{'Content-Type':'application/json'},
#           body: JSON.stringify(payload)
#         });
#         const body = await res.json();
#         if (body.error) {
#           output.textContent = 'Error: ' + body.error;
#         } else {
#           // pretty-print JSON or markdown
#           output.textContent = typeof body.output === 'string'
#                               ? body.output
#                               : JSON.stringify(body.output, null, 2);
#         }
#       } catch(err) {
#         output.textContent = 'Network error: ' + err.message;
#       } finally {
#         spinner.style.display = 'none';
#         runBtn.disabled = false;
#       }
#     };
#   </script>
# </body>
# </html>
# """

# @app.route("/", methods=["GET"])
# def index():
#     return render_template_string(INDEX_HTML)

# @app.route("/api/run", methods=["POST"])
# def api_run():
#     data = request.get_json(force=True) or {}
#     crew = RealestatepacketcrewAutomationProjectSetupGuideCrew().crew()
#     try:
#         result = crew.kickoff(inputs=data)
#         return jsonify({"output": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port, debug=True)
# import io
# import logging
# from flask import Flask, render_template, request, jsonify, send_file
# from crew import RealestatepacketcrewAutomationProjectSetupGuideCrew

# # -------------- Setup logging -------------- #
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s %(message)s"
# )
# logger = logging.getLogger(__name__)

# # -------------- Flask app -------------- #
# app = Flask(
#     __name__,
#     static_folder="assets",
#     static_url_path="/assets",
#     template_folder="templates"
# )

# @app.route("/", methods=["GET"])
# def index():
#     # you move your full HTML into templates/index.html
#     return render_template("index.html")


# @app.route("/api/run", methods=["POST"])
# def api_run():
#     # 1) Load every field your UI sends
#     payload = request.get_json(force=True, silent=True)
#     if not payload:
#         return jsonify({"error": "Invalid or missing JSON body"}), 400

#     # 2) Log it so you can inspect in your journalctl/gunicorn logs
#     logger.info("→ /api/run payload: %s", payload)

#     # 3) Kick off your crew with exactly that payload
#     crew = RealestatepacketcrewAutomationProjectSetupGuideCrew().crew()
#     try:
#         result = crew.kickoff(inputs=payload)
#     except Exception as e:
#         # 4) If anything blows up (including missing template vars),
#         #    log the full stack trace and return a JSON 500.
#         logger.exception("Crew kickoff failed")
#         return jsonify({
#             "error": "Crew execution failed",
#             "details": str(e)
#         }), 500

#     # 5) Normalize result to string
#     output = result if isinstance(result, str) else str(result)
#     return jsonify({"output": output.strip()})


# # (You can keep your other static/templated routes here,
# #  e.g. "/how-it-works", "/agents", etc.)


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
from flask import Flask, render_template, request, jsonify
from crew import RealestatepacketcrewAutomationProjectSetupGuideCrew

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.get_json() or {}
    crew = RealestatepacketcrewAutomationProjectSetupGuideCrew().crew()
    try:
        # Kick off the crew with exactly the JSON payload from the front end
        result = crew.kickoff(inputs=data)
        # Crew may return a str or some other object—coerce to str
        markdown = result if isinstance(result, str) else str(result)
        return jsonify({"output": markdown})
    except Exception as e:
        # In case the crew blows up, return the error message
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
