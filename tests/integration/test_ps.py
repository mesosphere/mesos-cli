
import mock

import mesos.cli.ps

from .. import utils

@mock.patch("mesos.cli.slave.MesosSlave.stats", utils.slave_stats)
class TestPs(utils.MockState):

    @utils.patch_args([
        "mesos-ps"
    ])
    def test_format(self):
        mesos.cli.ps.main()

        # Time
        assert "01:23.33" in self.stdout
        # RSS
        assert "10.46 MB" in self.stdout
        # CPU
        assert "0.1" in self.stdout
        # MEM
        assert "65.41" in self.stdout
        # Command
        assert "while true" in self.stdout
        # User
        assert "root" in self.stdout
        # PID
        assert "app-215.3e" in self.stdout

        assert len(self.lines) == 4

    @utils.patch_args([
        "mesos-ps",
        "-i"
    ])
    def test_inactive(self):
        mesos.cli.ps.main()

        assert len(self.lines) == 17
