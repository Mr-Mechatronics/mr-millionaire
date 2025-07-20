"""Memory DB handler."""

import sqlite3

import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings


class MemoryHandler:

    """Memory DB handler."""

    SIM_THRESHOLD = 0.85

    def __init__(self) -> None:
        """Constructor for Memory DB handler."""
        self.conn = sqlite3.connect("memory.db")
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS qa (
                   id        INTEGER PRIMARY KEY AUTOINCREMENT,
                   question  TEXT  UNIQUE,
                   answer    TEXT,
                   embedding BLOB
               )""",
        )
        self.conn.commit()

    def already_seen(self, question: str) -> bool:
        """Return True if this exact wording is already in the DB.

        Args:
            question (str): The question to check.

        Returns:
            bool: True if this exact wording is already in the DB.

        """
        row = self.conn.execute(
            "SELECT 1 FROM qa WHERE question = ?", (question,),
        ).fetchone()
        return row is not None

    def clear_memory(self) -> None:
        """Clear memory."""
        self.conn.execute("DELETE FROM qa")
        self.conn.commit()

    def embed(self, text: str) -> list[float]:
        """Embed text into memory.

        Args:
            text (str): The text to embed.

        Returns:
            list[float]: List of embedded words.

        """
        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return embedder.embed_query(text)

    def is_semantic_duplicate(self, question: str) -> bool:
        """Check if the question is similar to the one in the database.

        Args:
            question (str): The question to check.

        Returns:
            bool: True if the question is similar to the one in the database.

        """
        new_vec = np.array(self.embed(question))
        for (old_vec_blob,) in self.conn.execute("SELECT embedding FROM qa WHERE embedding IS NOT NULL"):
            old_vec = np.frombuffer(old_vec_blob, dtype=np.float32)
            sim = np.dot(new_vec, old_vec) / (np.linalg.norm(new_vec) * np.linalg.norm(old_vec))
            if sim >= self.SIM_THRESHOLD:
                return True
        return False

    def save_with_embedding(self, question: str, answer: str, vector: list[float]) -> None:
        """Save a question and answer to the database.

        Args:
            question (str): The question to save.
            answer (str): The answer.
            vector (list[float]): The vector to store in the database.

        """
        self.conn.execute(
            "INSERT INTO qa (question, answer, embedding) VALUES (?, ?, ?)",
            (question, answer, np.array(vector, dtype=np.float32).tobytes()),
        )
        self.conn.commit()
