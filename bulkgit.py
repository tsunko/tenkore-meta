from glob import glob
import sys
import subprocess

if len(sys.argv) < 2:
    sys.exit('Usage: %s git-command' % sys.argv[0])

path = "*/"
ignore = []
argStart = 1
for i in range(0, len(sys.argv)):
    arg = sys.argv[i]
    if arg.startswith("-p:"):
        path = arg.split(":")[1]
        argStart += 1
    if arg.startswith("-i:"):
        ignore.append(arg.split(":")[1].lower())
        print("==> Set to ignore " + arg.split(":")[1], flush=True)
        argStart += 1
        
repos = glob(path)
for repo in repos:
    if(repo.lower()[:-1] in ignore):
        print("==> Ignoring " + repo, flush=True)
        continue
    args = ' '.join(sys.argv[argStart:]).strip();
    print("==> Performing \"" + args + "\" on repository " + repo, flush=True)
    subprocess.Popen(
        ["git"] + sys.argv[argStart:],
        stdout=subprocess.PIPE,
        cwd=repo
    ).communicate()
