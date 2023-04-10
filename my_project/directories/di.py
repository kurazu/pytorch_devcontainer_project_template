from injector import Module, provider, singleton

from .config import DirectoryConfig
from .interface import InputDir, OutputDir


class DirectoriesModule(Module):
    @singleton
    @provider
    def provide_input_dir(self, config: DirectoryConfig) -> InputDir:
        return InputDir(config.input_dir)

    @singleton
    @provider
    def provide_output_dir(self, config: DirectoryConfig) -> OutputDir:
        return OutputDir(config.output_dir)
