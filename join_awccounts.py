import pandas as pd

df = pd.DataFrame(columns=["corpus", "sample_id", "AWC", "CTC", "CVC"])

berg = pd.read_csv("idsads_file_awccvc_Bergelson.csv")
warl = pd.read_csv("idsads_file_awccvc_Warlaumont.csv")
# mcdv = pd.read_csv("idsads_file_awccvc_McDivitt.csv")
vand = pd.read_csv("idsads_file_awccvc_VanDam.csv")

berg["corpus"] = "Bergelson"
warl["corpus"] = "Warlaumont"
vand["corpus"] = "VanDam"

berg["sample_id"] = "B-" + berg.file.str[:2]
warl["sample_id"] = "W-" + warl.file.str[1:4]
vand["sample_id"] = "V-" + vand.file.str[:4]

berg = berg[["corpus", "sample_id", "AWC", "CTC", "CVC"]]
warl = warl[["corpus", "sample_id", "AWC", "CTC", "CVC"]]
vand = vand[["corpus", "sample_id", "AWC", "CTC", "CVC"]]

berg.AWC = berg.AWC.astype(int)
warl.AWC = warl.AWC.astype(int)
vand.AWC = vand.AWC.astype(int)

df = df.append([berg, warl, vand])

df.to_csv("idsads_awccvc.csv", index=False)

print
