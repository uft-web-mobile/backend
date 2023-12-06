import os
import subprocess


def execute_python(code):
    process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return stdout, stderr


# def execute_c(code):
#     try:
#         process = subprocess.run(["gcc", "-o", "./program", "-x", "c", "-"], input=code, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        
#         # Se a compilação for bem-sucedida (sem exceção lançada), execute o programa
#         execution = subprocess.run(["./program"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

#         # Remover o arquivo executável
#         os.remove("./program")

#         return execution.stdout, execution.stderr

#     except subprocess.CalledProcessError as compile_error:
#         # Erro de compilação
#         return None, f"Compilation Error: {compile_error.stderr}"

#     except Exception as e:
#         # Outros erros
#         return None, f"Error: {str(e)}"

    

def execute_javascript(code):
    process = subprocess.Popen(["node", "-e", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return stdout, stderr

