# 🦫 bobersay

A zero-dependency `cowsay` clone for Unix/Linux/macOS terminals featuring an authentic Polish **bóbr**.

```text
 __________________
< Ale fajny bober! >
 ------------------
       \
        \     _.-"""-._
         \   ( )     ( )
             /  o   o  \
            |    (_)    |
            |  .'|_|'.  |       _..---.._
           /     '-'     \   .-'#########'-.
          |   (_     _)   |.'###############'.
          |     '---'     |###################)
           \             / '-.#############.-'
           _'-.._____..-'_    ''--.....--''
          (_____)   (_____)
```

## Features

- **Zero dependencies** — pure Python 3 standard library.
- **Built-in Polish bóbr quotes** — run `bobersay` with no arguments for a random classic quote.
- **Pipe support** — works seamlessly with `echo`, `fortune`, `cat`, and other CLI tools.
- **`cowsay`-compatible flags** — supports dead (`-d`), greedy (`-g`), custom eyes (`-e`), thought bubbles (`-t`), and custom line wrapping (`-W`).

## Installation

### Quick Install (User `$PATH`)

```bash
git clone https://github.com/YOUR_USERNAME/bobersay.git
cd bobersay
chmod +x bobersay.py
mkdir -p ~/.local/bin
cp bobersay.py ~/.local/bin/bobersay
```

*(Make sure `~/.local/bin` is in your `$PATH`, or copy it to `/usr/local/bin/bobersay` using `sudo`.)*

### Run Directly

```bash
python3 bobersay.py "Ale fajny bober!"
```

## Usage

```bash
# Random Polish bóbr quote
bobersay

# Custom message
bobersay "Patrzcie jaki wielki bóbr!"

# Greedy eyes ($)
bobersay -g "Darmowe drewno!"

# Dead eyes (x)
bobersay -d "O kurwa, gryzie!"

# Thought bubble
bobersay -t "Time to build a dam..."

# Pipe output from another command
fortune | bobersay
```

## CLI Options

| Flag | Long Flag | Description |
| :--- | :--- | :--- |
| `-W` | `--width` | Max width of the speech bubble before wrapping (default: `40`) |
| `-e` | `--eyes` | Custom single-character eyes (default: `o`) |
| `-d` | `--dead` | Use `x` eyes |
| `-g` | `--greedy` | Use `$` eyes |
| `-t` | `--think` | Render a thought bubble instead of a speech bubble |
| `-v` | `--version` | Show program version |
| `-h` | `--help` | Show help message |

## License

MIT
