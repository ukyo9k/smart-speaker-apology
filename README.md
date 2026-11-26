# Sorry, I Heard That Wrong — a smart speaker apologises

[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/ukyo9k/smart-speaker-apology/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/ukyo9k/smart-speaker-apology/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

Entry for the [make.fun bounty "Sorry, I Heard That Wrong"](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729): write the funniest one-line apology a smart speaker gives its owner after mishearing them (at most 140 characters).

## The line

> Sorry — I heard 'turn it down' as 'burn it down'. I've lowered the volume and cancelled the arson.

98 characters. The speaker mishears a volume request as an arson request, then reports — in the flat, helpful voice of a device — that it has quietly handled both.

## How it works

`main.py` (Python 3, standard library only, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
