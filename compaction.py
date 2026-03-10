def compact(files):

    merged = {}

    for file in files:

        with open(file) as f:

            for line in f:

                k, v = line.strip().split(":")
                merged[k] = v

    merged = sorted(merged.items())

    new_file = "storage/compact.db"

    with open(new_file, "w") as f:

        for k, v in merged:

            if v != "__TOMBSTONE__":
                f.write(f"{k}:{v}\n")

    return new_file