import asyncio
from abc import ABC, abstractmethod
from asyncio.log import logger
from Pathlib import Path
from config.logging_config import setup_logger

logger = setup_logger(__name__)

class BaseDocumentLoader(ABC):
    def __init__(self, path: str | Path):
        self.path = Path(path)

    @abstractmethod
    async def load(self) -> str:
        pass

#reads .txt file format
class TextLoader(BaseDocumentLoader):
    async def load(self) -> str:
        logger.info(f"loading text file: {self.path.name}")
        if not self.path.exists():
            logger.error(f"File not found: {self.path.name}")

        loop = asyncio.get_event_loop()

        def _read_file():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.error(f"Error reading text file {self.path.name}: {e}")
                raise
        return await loop.run_in_executor(None, _read_file)

# reads .md file format

class MarkDownLoader(BaseDocumentLoader):
    """
    A document loader for reading markdown files.
    """

    async def load(self) -> str:
        logger.info(f"loading markdown file: {self.path.name}")
        if not self.path.exists():
            logger.error(f"File not found: {self.path.name}")

        loop = asyncio.get_event_loop()

        def _read_file():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.error(f"Error reading markdown file {self.path.name}: {e}")
                raise

        return await loop.run_in_executor(None, _read_file)
    
class PdfLoader(BaseDocumentLoader):
    """
    A document loader for pdf files
    """

    async def load(self) -> str:
        logger.info(f"loading pdf file: {self.path.name}")
        if not self.path.exists():
            logger.error(f"File not found: {self.path.name}")

        loop = asyncio.get_event_loop()

        def _read_file():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.error(f"Error reading pdf file {self.path.name}: {e}")
                raise

        return await loop.run_in_executor(None, _read_file)

# TODO: Reads .docx file format. Once docx loader is implemented, it can be added to the DocumentLoadFactory.
# TODO: Reads .doc file format
# TODO: Reads .pdfOcr file format

class DocumentLoadFactory:

    @staticmethod
    def get_loader(path: str | Path) -> BaseDocumentLoader:
        """
        Factory method to return the appropriate document loader based on file extension.
        """
        path = Path(path)
        if not path.exists():
            logger.error(f"File not found: {path.name}")
            raise FileNotFoundError(f"File not found: {path.name}")

        if path.suffix == ".txt":
            return TextLoader(path)
        elif path.suffix == ".md":
            return MarkDownLoader(path)
        elif path.suffix == ".pdf":
            return PdfLoader(path)
        # elif path.suffix == ".docx":
        #     return DocxLoader(path)
        # elif path.suffix == ".doc":
        #     return DocLoader(path)
        # elif path.suffix == ".pdfOcr":
        #     return PdfOcrLoader(path)
        else:
            logger.error(f"Unsupported file format: {path.suffix} for file {path.name}")
            raise ValueError(f"Unsupported file format: {path.suffix}")