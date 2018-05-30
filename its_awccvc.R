library(rlena)
library(tidyverse)

its_dir <- 'data/its_other/VanDam'

files <- list.files(its_dir, pattern="*.its", full.names = T)

df <- tibble()

for (x in files) {
  its <- read_its_file(x)
  row <- its %>%
    gather_blocks() %>%
    group_by(itsId) %>%
    summarise(
      file = basename(x),
      AWC = sum(adultWordCnt, na.rm = TRUE),
      CTC = sum(turnTaking, na.rm = TRUE),
      CVC = sum(childUttCnt, na.rm = TRUE))
  df <- rbind(df, row)
}

df <- select(df, -itsId)

write_csv(df, "idsads_file_awccvc.csv")
