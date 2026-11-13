def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)
# TODO 1: File processor with complete error handling

    def process_file(filename):
        file = None
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print(f" File not found: {filename}")
            return None
        except PermissionError:
            print(f" Permission Denied: {filename}")
        else:
            content = file.read()
            return content.strip().upper()
        finally:
            if file is not None:
                file.close()
                print(f" Closed '{filename}'")
# Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")
# TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name, should_fail=False):
            self.name = name
            self.should_fail = should_fail
            self.resource = None
        
        def acquire(self):
            """Acquire resource - might fail."""
            if self.should_fail:
                raise RuntimeError(f"Could not acquire {self.name}")
            self.resource = f"{self.name} connection"
            print(f" Acquired {self.resource}")
    

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                print(f" Released {self.resource}")
                self.resource = None
            else:
                print(f" Nothing to release for {self.name}")
        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError("Resource not acquired")
            print(f" Using {self.resource}")


# Test resource management
    rm = ResourceManager("Database")
    try:
        rm.acquire()
    except RuntimeError as e:
        print(f" Acquire failed: {e}")
    else:
        rm.use()
    finally:
        rm.release()


practice_3_complete_pattern()




def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)
    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass
    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"{reason} at {position}")
    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Winner is {winner}")
        
# TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
        def make_move(self, row, col):
            # 1. Game already finished?
            if self.game_over:
                raise GameOverError(self.current_player)

            # 2. Out of bounds (check BEFORE touching the board)
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "Position out of bounds")

            # 3. Already taken?
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position already taken")

            # Valid move: place the mark and switch players
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

# Test the game
    game = TicTacToe()
    test_moves = [
    (0, 0), # Valid
    (0, 0), # Already taken
    (5, 5), # Out of bounds
    ]
    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")
# Run the practice
practice_2_custom_exceptions()


def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)
    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []
        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None
            try:
                file = open(filename, "r")
                content = file.read()
            except FileNotFoundError:
                print(f"  File not found: {filename}")
                self.failed_files.append((filename, "File not found"))
                return None
            except PermissionError:
                print(f"  Permission denied: {filename}")
                self.failed_files.append((filename, "Permission denied"))
                return None
            except Exception as e:
                print(f"  Unexpected error with {filename}: {e}")
                self.failed_files.append((filename, f"Unexpected error: {e}"))
                return None
            else:
                # Only runs if open() and read() both worked
                self.processed_files.append(filename)
                print(f"  Processed {filename}")
                return content.strip()
            finally:
                # Always runs, even after the returns above
                if file is not None:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            import os

            try:
                names = os.listdir(directory)
            except (FileNotFoundError, PermissionError) as e:
                print(f"  Cannot read directory {directory}: {e}")
                self.failed_files.append((directory, str(e)))
                return

            for name in names:
                path = os.path.join(directory, name)
                if os.path.isfile(path):
                    self.process_file(path)

        def get_report(self):
            """
            Get processing report.
            """
            return {
                "processed": len(self.processed_files),
                "failed": len(self.failed_files),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files,
            }
        # Test the processor
    processor = FileProcessor()
    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")
# Run the practice
practice_3_complete_system()