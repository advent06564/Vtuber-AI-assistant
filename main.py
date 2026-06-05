"""Vtuber AI Assistant - CLI entry point.

A modular, extensible framework for a hybrid assistant with a
custom VTuber front-end driven by an AI model of your choice
(API, cloud LLM, or local model).

Usage:
    python main.py chat          # interactive chat
    python main.py status        # show configuration
"""

import sys


class VtuberAI:
    """Core Vtuber AI assistant class."""

    def __init__(self, name: str = "Aurora"):
        self.name = name
        self.running = False

    def status(self) -> dict:
        """Report the current state of the assistant."""
        return {
            "name": self.name,
            "running": self.running,
            "mode": "CLI",
            "version": "0.2.0",
        }

    def chat(self) -> None:
        """Simple interactive chat loop (CLI demo)."""
        self.running = True
        print(f"\n  {self.name} AI Assistant - type 'exit' to quit\n")
        while self.running:
            try:
                user_input = input("  You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n  Goodbye!")
                break

            if user_input.lower() in ("exit", "quit", "q"):
                print(f"  {self.name}: Goodbye!")
                break
            elif user_input:
                # Placeholder - swap in your AI backend here
                print(f"  {self.name}: [echo] {user_input}")
        self.running = False

    def main(self) -> None:
        """Entry point with subcommand support."""
        if len(sys.argv) > 1:
            cmd = sys.argv[1].lower()
        else:
            cmd = "chat"

        if cmd == "chat":
            self.chat()
        elif cmd == "status":
            info = self.status()
            for k, v in info.items():
                print(f"  {k}: {v}")
        else:
            print(f"  Unknown command: {cmd}")
            print("  Usage: python main.py [chat|status]")


# Script entry point

if __name__ == "__main__":
    ai = VtuberAI()
    ai.main()