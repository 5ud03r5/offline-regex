import { shallowMount } from "@vue/test-utils";

import RegexRegistry from "../components/pages/RegexRegistry.vue";
import RegistryItem from "../components/RegistryItem.vue";
import UniversalTag from "../components/UI/UniversalTag.vue";

describe("RegexRegistry.vue", () => {
  test("regex items rendering", () => {
    const filteredRegex = [{}, {}, {}, {}];
    const wrapper = shallowMount(RegexRegistry, {
      setup() {
        return {
          filteredRegex: filteredRegex,
        };
      },
    });
    const items = wrapper.findAllComponents(RegistryItem);
    expect(items).toHaveLength(filteredRegex.length);
  });

  test("tags items rendering", () => {
    const tags = [{}, {}, {}, {}];
    const wrapper = shallowMount(RegexRegistry, {
      setup() {
        return {
          tags: tags,
        };
      },
    });
    const items = wrapper.findAllComponents(UniversalTag);
    expect(items).toHaveLength(tags.length);
  });

  test("search functionality", async () => {
    const search = "qwe";
    const data = [
      { name: "qwer" },
      { name: "qqwer" },
      { name: "awer" },
      { name: "qwor" },
    ];

    const wrapper = shallowMount(RegexRegistry, {
      setup() {
        return {
          data: data,
          search: search,
          filteredRegex: data.filter((item) => item.name.includes(search)),
        };
      },
    });
    const items = wrapper.findAllComponents(RegistryItem);
    expect(items).toHaveLength(2);
  });

  test.todo("tag filtering", async () => {
    const tags = [{ name: "one" }, { name: "two" }, { name: "three" }];
    const filteredRegex = [
      { tags: ["one"] },
      { tags: ["one", "two"] },
      { tags: ["three", "one"] },
      { tags: ["two"] },
    ];
    const filter = [];
    const setFilter = (item) => {
      console.log(item.name);
      if (filter.includes(item.name)) {
        const index = filter.indexOf(item.name);
        filter.splice(index, 1);
      } else {
        filter.push(item.name);
      }
    };

    const wrapper = shallowMount(RegexRegistry, {
      setup() {
        return {
          tags: tags,
          filteredRegex: filteredRegex,
          filter,
          setFilter,
        };
      },
    });
    await wrapper.findComponent('[tag="two"]').trigger("click");
    const items = wrapper.findAllComponents(RegistryItem);
    expect(items).toHaveLength(2);
  });
});
