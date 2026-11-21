import os


POEM = """May I? My knuckles sting.
You lift the latch. Come in.
A hand places a key in my palm;
I turn it once, then set it down.
When they ask me to stay,
I hear the hinge in my own wrist:
permission is not a leash—
it is the thing I can return,
and still open."""


output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry:
    entry.write(POEM)
