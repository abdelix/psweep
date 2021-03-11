#!/usr/bin/env python3

import numpy as np
import psweep as ps

if __name__ == "__main__":
    df = ps.df_read("calc/database.pk")

    func = lambda fn: np.load(fn)
    arr = np.array(
        [func(f"calc/{pset_id}/out.npy") for pset_id in df._pset_id.values]
    )

    df["mean"] = arr.mean(axis=1)

    cols = ["param_a", "param_b", "mean"]
    ps.df_print(df[cols])

    ps.df_write(df, "calc/database_eval.pk")
