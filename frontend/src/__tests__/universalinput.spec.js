import { shallowMount } from "@vue/test-utils";
import UniversalInput from "../components/UI/UniversalInput.vue";

describe("UniversalInput.vue", () => {
  test("input value emits", async () => {
    const wrapper = shallowMount(UniversalInput, {
      props: {
        value: "init",
        "onUpdate:value": (e) => wrapper.setProps({ value: e }),
      },
    });

    await wrapper.find("input").setValue("test");
    expect(wrapper.props("value")).toBe("test");
  });
});
