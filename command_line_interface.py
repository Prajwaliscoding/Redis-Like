import argparse
from key_value_store import KVStore

kv = KVStore()

def main():
    parser = argparse.ArgumentParser(description="Key-Value Store CLI")
    parser.add_argument("--set", nargs=2, metavar=("key", "value"))
    parser.add_argument("--get", metavar="key")

    args = parser.parse_args()
    if args.set:
        kv.set(args.set[0], args.set[1])
        print(f"Set {args.set[0]} = {args.set[1]}")
    elif args.get:
        print(kv.get(args.get))

if __name__ == "__main__":
    main()