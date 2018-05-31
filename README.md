# Openstack Replays

Toolset for restoring openstack volumes via replays when using Openstack Cinder in conjunction with a Dell SMC solution.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Docker >= 17
Docker-compose >= 1.20.0
```

### Installing

Build the app
```
docker-compose build
```

Once built execute the run file:
```
# ./run.sh
```

## Running the tests

There is currently no tests to run.


## Built With

[Openstack SDK](https://docs.openstack.org/openstacksdk/) Python SDK for Openstack as a whole.
[InfiniDat Munch](https://github.com/Infinidat/munch) A Munch is a Python dictionary that provides attribute-style access (a la JavaScript objects).
[Dell Base Flock Driver](https://github.com/dellstorage/storagecenter-flocker-driver) *WARNING* I Have modified this as a number of methods and endpoints do not exist*
[NPYScreen](http://npyscreen.readthedocs.io/) for my UI

## Contributing

Fork, modify and submit a pull request. Simple.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.realworld.net.au/realworldtech/openstack_replays/tags).

## Authors

* **Karl Kloppenborg** - *Initial work* - [inventionlabsSydney](https://github.com/inventionlabsSydney)

See also the list of [contributors](https://github.realworld.net.au/realworldtech/openstack_replays/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

* Dell Storage Solutions for base api code.
* Andrew Yager [andrewyager](https://github.com/andrewyager) for discovering the createView and list_replays requirements I needed)

--Karl
