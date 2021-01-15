set -e

for dir in lib include local bin share; do
    if [ -d "$dir" ]; then
        rm -r "$dir"
    fi
done

python3 -m venv .
./bin/pip install pyramid==1.9.4
./bin/pip install repoze.zcml==1.1
./bin/pip install repoze.workflow==1.1
./bin/pip install -e .
